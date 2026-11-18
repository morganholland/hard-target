"""Check the built editions against docs/PLAN-formats.md. Run after build_editions.py.

Each test names the requirement it covers. Exit code is non-zero if any test fails.
"""

import re
import subprocess
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
DIST = ROOT / "dist"
CHAPTERS = sorted((ROOT / "chapters").glob("*.md"))
LICENSE_NAME = "CC BY-NC 4.0"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.links, self.rels, self.pres, self.scripts = set(), [], {}, 0, []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        if tag == "a" and "href" in a:
            self.links.append(a["href"])
            for rel in (a.get("rel") or "").split():
                self.rels[rel] = a["href"]
        if tag == "pre":
            self.pres += 1
        if tag == "script" and a.get("src"):
            self.scripts.append(a["src"])


def page_name(chapter):
    return chapter.stem + ".html"


def test_r1_site_pages():
    missing = [p for p in ["index.html", "sources.html"] + [page_name(c) for c in CHAPTERS]
               if not (SITE / p).exists()]
    assert not missing, f"missing pages: {missing}"


def test_r2_navigation():
    names = [page_name(c) for c in CHAPTERS]
    for i, name in enumerate(names):
        page = Page(SITE / name)
        assert page.links.count("index.html") >= 2, f"{name}: no Contents link in the chapter navigation"
        if i > 0:
            assert page.rels.get("prev") == names[i - 1], f"{name}: prev link is {page.rels.get('prev')}"
        if i < len(names) - 1:
            assert page.rels.get("next") == names[i + 1], f"{name}: next link is {page.rels.get('next')}"


def test_r3_links_resolve():
    pages = {p.name: Page(p) for p in SITE.glob("*.html")}
    broken = []
    for name, page in pages.items():
        for href in page.links:
            parts = urlsplit(href)
            if parts.scheme or href.startswith(("mailto:", "//")):
                continue
            target = unquote(parts.path) or name
            if target.endswith(".md"):
                broken.append(f"{name}: Markdown link {href}")
                continue
            if not (SITE / target).exists():
                broken.append(f"{name}: {href}")
            elif parts.fragment and target in pages and parts.fragment not in pages[target].ids:
                broken.append(f"{name}: {href} (no such anchor)")
    assert not broken, "broken links:\n  " + "\n  ".join(broken)


def test_r4_prompt_blocks():
    page = Page(SITE / "15-agent-prompt-library.html")
    prompts = sorted((ROOT / "prompts").glob("P*-*.md"))
    assert page.pres == len(prompts) + 1, f"{page.pres} code blocks, expected {len(prompts) + 1} (rules + prompts)"
    for prompt in prompts:
        anchor = re.sub(r"[^\w -]", "", prompt.read_text(encoding="utf-8").splitlines()[0][2:].lower()).replace(" ", "-")
        assert anchor in page.ids, f"prompt section #{anchor} missing from the prompt library page"
    assert "shared-rules" in page.ids
    assert "copy.js" in page.scripts, "copy.js is not loaded"
    assert (SITE / "copy.js").exists()


def test_r5_downloads():
    page = Page(SITE / "index.html")
    for f in ["downloads/hard-target.pdf", "downloads/hard-target.epub"]:
        assert f in page.links, f"index does not link {f}"
        assert (SITE / f).stat().st_size > 50_000, f"{f} is missing or too small"


def test_r6_pdf():
    from pypdf import PdfReader

    reader = PdfReader(SITE / "downloads/hard-target.pdf")
    box = reader.pages[0].mediabox
    assert (round(float(box.width)), round(float(box.height))) == (612, 792), "not US Letter"
    top = [o for o in reader.outline if not isinstance(o, list)]
    titles = [o.title for o in top]
    for chapter in CHAPTERS:
        title = chapter.read_text(encoding="utf-8").splitlines()[0].removeprefix("# ")
        assert title in titles, f"PDF outline lacks '{title}'"
    assert len(reader.pages) > 30, f"only {len(reader.pages)} pages"
    assert LICENSE_NAME in " ".join((p.extract_text() or "") for p in reader.pages[:4]), "PDF lacks the license notice"
    # Prompt blocks and tables must stay inside the right margin (0.9in on Letter = 547.2pt).
    bbox = subprocess.run(["pdftotext", "-bbox", str(SITE / "downloads/hard-target.pdf"), "-"],
                          capture_output=True, text=True, check=True).stdout
    widest = max(float(x) for x in re.findall(r'xMax="([\d.]+)"', bbox))
    assert widest <= 547.2 + 2, f"text runs past the right margin (x = {widest:.1f}pt)"


def epubcheck(path):
    result = subprocess.run([sys.executable, "-m", "epubcheck", str(path)], capture_output=True, text=True)
    out = result.stdout + result.stderr
    errors = [l for l in out.splitlines() if l.startswith(("ERROR", "FATAL"))]
    assert result.returncode == 0 and not errors, f"epubcheck failed for {path.name}:\n" + "\n".join(errors or [out[-2000:]])


def opf_and_nav(path):
    with zipfile.ZipFile(path) as z:
        assert z.namelist()[0] == "mimetype", "mimetype must be the first entry"
        container = z.read("META-INF/container.xml").decode()
        opf_path = re.search(r'full-path="([^"]+)"', container)[1]
        opf = z.read(opf_path).decode()
        nav_href = re.search(r'<item[^>]*properties="nav"[^>]*>', opf)[0]
        nav_href = re.search(r'href="([^"]+)"', nav_href)[1]
        base = opf_path.rsplit("/", 1)[0] + "/" if "/" in opf_path else ""
        nav = z.read(base + nav_href).decode()
        return opf, nav, z.namelist()


def test_r7_epub():
    path = DIST / "hard-target.epub"
    epubcheck(path)
    _, nav, _ = opf_and_nav(path)
    toc = nav.split('epub:type="toc"', 1)[1].split("</nav>", 1)[0]
    for chapter in CHAPTERS:
        title = chapter.read_text(encoding="utf-8").splitlines()[0].removeprefix("# ")
        assert title.replace("&", "&amp;") in toc, f"EPUB contents lacks '{title}'"
    assert (SITE / "downloads/hard-target.epub").read_bytes() == path.read_bytes()


def test_r8_kindle_epub():
    path = DIST / "hard-target-kindle.epub"
    epubcheck(path)
    opf, _, names = opf_and_nav(path)
    assert re.search(r'<item[^>]*properties="cover-image"', opf), "no cover-image item"
    assert not any(n.endswith("cover.xhtml") for n in names), "separate HTML cover page present"
    for tag in ["dc:title", "dc:creator", "dc:language", "dc:date", "dc:description"]:
        assert f"<{tag}" in opf, f"missing {tag}"
    assert "Morgan Holland" in opf


def test_r9_cover():
    from PIL import Image

    with Image.open(ROOT / "assets/cover.jpg") as img:
        assert img.format == "JPEG" and img.mode == "RGB", f"{img.format} {img.mode}"
        assert img.size == (1600, 2560), f"cover is {img.size}"


def test_r10_kdp_kit():
    listing = (ROOT / "kdp/listing.md").read_text(encoding="utf-8")
    for heading in ["Title", "Description", "Keywords", "Categories", "Price", "AI-generated content"]:
        assert f"## {heading}" in listing, f"kdp/listing.md lacks '## {heading}'"
    keywords = listing.split("## Keywords", 1)[1].split("##", 1)[0]
    count = len([l for l in keywords.splitlines() if l.startswith(("- ", "1", "2", "3", "4", "5", "6", "7"))])
    assert count == 7, f"KDP allows 7 keywords, found {count}"


def test_r11_ci():
    workflow = (ROOT / ".github/workflows/editions.yml").read_text(encoding="utf-8")
    assert "pull_request:" in workflow, "editions are not built on pull requests"
    assert "python3 scripts/build_editions.py" in workflow and "python3 scripts/test_editions.py" in workflow
    deploy = workflow.split("\n  deploy:", 1)[1]
    assert "github.ref == 'refs/heads/main'" in deploy.split("steps:", 1)[0], "deploy is not limited to main"
    assert "pages: write" in deploy and "actions/deploy-pages" in deploy
    upload = workflow.split("upload-pages-artifact", 1)[0].rsplit("- ", 1)[1]
    assert "refs/heads/main" in upload, "the Pages artifact is uploaded from branches other than main"


def test_r12_license():
    assert LICENSE_NAME in (ROOT / "LICENSE.md").read_text(encoding="utf-8")
    assert LICENSE_NAME in (SITE / "index.html").read_text(encoding="utf-8")
    for epub in ["hard-target.epub", "hard-target-kindle.epub"]:
        with zipfile.ZipFile(DIST / epub) as z:
            text = " ".join(z.read(n).decode("utf-8", "ignore") for n in z.namelist() if n.endswith(".xhtml"))
        assert LICENSE_NAME in text, f"{epub} lacks the license notice"


def main():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for test in tests:
        try:
            test()
            print(f"PASS {test.__name__}")
        except Exception as error:  # report every failure, not just the first
            failed += 1
            print(f"FAIL {test.__name__}: {error}")
    print(f"{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
