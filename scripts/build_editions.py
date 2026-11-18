"""Build the website (site/), the PDF, the EPUB and the Kindle EPUB (dist/) from the chapter files.

Needs pandoc 3.1+, WeasyPrint and Python 3.11+. Run scripts/build_manual.py first if MANUAL.md
is stale; this script refuses to build from a stale copy.
"""

import html
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_manual  # noqa: E402

SITE, DIST, ASSETS, WEB = ROOT / "site", ROOT / "dist", ROOT / "assets", ROOT / "web"
CHAPTERS = sorted((ROOT / "chapters").glob("*.md"))
PROMPTS = ROOT / "prompts"
LIBRARY_PAGE = "15-agent-prompt-library.html"

TITLE = "Hard Target"
SUBTITLE = "The 2026 Field Manual for Digital Privacy"
AUTHOR = "Morgan Holland"
EDITION_DATE = "2026-11-18"
EDITION_DATE_TEXT = "18 November 2026"
SITE_URL = "https://morganholland.github.io/hard-target/"
REPO_URL = "https://github.com/morganholland/hard-target"
LICENSE_NAME = "CC BY-NC 4.0"
LICENSE_URL = "https://creativecommons.org/licenses/by-nc/4.0/"
DESCRIPTION = (
    "You cannot be invisible in 2026, but you can be a hard target: expensive to scam, slow to "
    "find, and quick to recover. Seventeen short chapters cover passkeys, SIM-swap locks, data "
    "brokers, credit freezes, AI voice-clone scams, connected cars, smart homes and what to do "
    "in the first hour after you are hit, with paste-ready prompts that let an AI agent do the "
    "legwork while you stay in control."
)


def heading(markdown):
    return markdown.splitlines()[0].removeprefix("# ").strip()


def prose_sub(markdown, pattern, repl):
    """Apply a regex substitution outside fenced code blocks only."""
    chunks = markdown.split("```")
    for i in range(0, len(chunks), 2):
        chunks[i] = re.sub(pattern, repl, chunks[i])
    return "```".join(chunks)


def pandoc(markdown, *args):
    result = subprocess.run(
        ["pandoc", "-f", "gfm", *args], input=markdown, capture_output=True, text=True, check=True
    )
    return result.stdout


# ---------------------------------------------------------------- website


def site_link_target(chapter, link):
    """Map a Markdown link in a chapter file to its page on the website."""
    path, _, fragment = link.partition("#")
    target = (chapter.parent / path).resolve()
    if target.parent == chapter.parent:
        page = target.stem + ".html"
    elif target == (ROOT / "SOURCES.md").resolve():
        page = "sources.html"
    elif target.parent == PROMPTS.resolve():
        anchor = "shared-rules" if target.name == "00-RULES.md" else build_manual.anchor(
            heading(target.read_text(encoding="utf-8"))
        ).lstrip("#")
        return f"{LIBRARY_PAGE}#{anchor}"
    else:
        raise ValueError(f"{chapter.name}: no website page for link {link}")
    return page + ("#" + fragment if fragment else "")


def site_shell(title, body, *, prev=None, next_=None, description=DESCRIPTION, script=False):
    nav = ['<a href="index.html">Contents</a>']
    if prev:
        nav.insert(0, f'<a rel="prev" href="{prev[0]}">← {html.escape(prev[1])}</a>')
    if next_:
        nav.append(f'<a rel="next" href="{next_[0]}">{html.escape(next_[1])} →</a>')
    nav_html = f'<nav class="pager" aria-label="Chapters">{" ".join(nav)}</nav>'
    copy = '<script src="copy.js" defer></script>' if script else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="stylesheet" href="style.css">
{copy}
</head>
<body>
<header class="masthead"><a href="index.html" class="brand">{TITLE}</a></header>
<main>
{body}
</main>
{nav_html if (prev or next_) else ""}
<footer>
<p>© 2026 {AUTHOR}. Licensed under <a href="{LICENSE_URL}">{LICENSE_NAME}</a>.
Source on <a href="{REPO_URL}">GitHub</a>. General security guidance, not legal or financial advice.</p>
</footer>
</body>
</html>
"""


def build_site():
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "downloads").mkdir(parents=True)
    shutil.copy(WEB / "style.css", SITE / "style.css")
    shutil.copy(WEB / "copy.js", SITE / "copy.js")
    shutil.copy(ASSETS / "cover.jpg", SITE / "cover.jpg")
    (SITE / ".nojekyll").write_text("")

    titles = [heading(c.read_text(encoding="utf-8")) for c in CHAPTERS]
    pages = [c.stem + ".html" for c in CHAPTERS]
    for i, chapter in enumerate(CHAPTERS):
        markdown = chapter.read_text(encoding="utf-8")
        markdown = prose_sub(
            markdown,
            r"\]\(([^():\s]+\.md(?:#[^)\s]*)?)\)",
            lambda m: "](" + site_link_target(chapter, m[1]) + ")",
        )
        body = pandoc(markdown, "-t", "html5", "--no-highlight")
        prev = (pages[i - 1], titles[i - 1]) if i else None
        next_ = (pages[i + 1], titles[i + 1]) if i + 1 < len(pages) else None
        page = site_shell(f"{titles[i]} · {TITLE}", body, prev=prev, next_=next_, script=chapter.name.startswith("15-"))
        (SITE / pages[i]).write_text(page, encoding="utf-8")

    sources = pandoc((ROOT / "SOURCES.md").read_text(encoding="utf-8"), "-t", "html5")
    (SITE / "sources.html").write_text(site_shell(f"Sources · {TITLE}", sources), encoding="utf-8")

    toc = "\n".join(f'<li><a href="{p}">{html.escape(t)}</a></li>' for p, t in zip(pages, titles))
    index = f"""
<section class="hero">
  <img src="cover.jpg" alt="Cover of Hard Target by Morgan Holland" width="320" height="512">
  <div>
    <h1>{TITLE}</h1>
    <p class="subtitle">{SUBTITLE}</p>
    <p>{html.escape(DESCRIPTION)}</p>
    <p class="downloads">
      <a class="button" href="00-start-here.html">Start reading</a>
      <a class="button secondary" href="downloads/hard-target.pdf">PDF</a>
      <a class="button secondary" href="downloads/hard-target.epub">EPUB</a>
    </p>
  </div>
</section>
<blockquote>
<p><strong>If someone may be monitoring you,</strong> read this site from a device they cannot reach, and start with the
<a href="00-start-here.html">safety note</a>. <strong>If you were just hit,</strong> go to
<a href="14-when-you-get-hit.html">chapter 14</a> now.</p>
</blockquote>
<h2>Contents</h2>
<ol class="toc">
{toc}
<li><a href="sources.html">Sources</a></li>
</ol>
<p class="edition">Facts and cases checked on {EDITION_DATE_TEXT}. Settings and menu labels change often, so
search an app's settings if a label has moved.</p>
"""
    (SITE / "index.html").write_text(site_shell(f"{TITLE}: {SUBTITLE}", index), encoding="utf-8")


# ---------------------------------------------------------------- books


def book_markdown(kindle):
    """MANUAL.md with chapters at level 1, front matter prepended, and checkboxes as plain bullets."""
    manual = (ROOT / "MANUAL.md").read_text(encoding="utf-8")
    body = manual.split("\n", 1)[1]  # drop the H1 title; the book metadata carries it
    body = prose_sub(body, r"(?m)^#(#{1,5}) ", r"\1 ")
    body = prose_sub(body, r"(?m)^(\s*)- \[ \] ", r"\1- ")
    edition = "Kindle edition" if kindle else "Free edition"
    online = "Online edition and updates" if kindle else "Read online, and get the PDF and EPUB"
    front = f"""# About this edition

**{TITLE}: {SUBTITLE}**, by {AUTHOR}. {edition}, {EDITION_DATE_TEXT}.

Copyright © 2026 {AUTHOR}. This work is licensed under [{LICENSE_NAME}]({LICENSE_URL}). You may share and adapt it for non-commercial purposes, with credit.

{online}: [{SITE_URL}]({SITE_URL})

Facts and cases were checked on {EDITION_DATE_TEXT}. Settings and menu labels change often. If one has moved, search the app's settings for the feature name. This is general security guidance, not legal or financial advice.

"""
    return front + body


def epub_metadata(kindle):
    return [
        "--metadata", f"title={TITLE}",
        "--metadata", f"subtitle={SUBTITLE}",
        "--metadata", f"author={AUTHOR}",
        "--metadata", "lang=en-US",
        "--metadata", f"date={EDITION_DATE}",
        "--metadata", f"description={DESCRIPTION}",
        "--metadata", f"rights=Copyright © 2026 {AUTHOR}. Licensed under {LICENSE_NAME}.",
        "--metadata", f"identifier={'urn:hard-target:kindle:2026-11-18' if kindle else 'urn:hard-target:free:2026-11-18'}",
    ]


def build_epub(kindle):
    out = DIST / ("hard-target-kindle.epub" if kindle else "hard-target.epub")
    subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "epub3", "-o", str(out), "--split-level=1", "--toc-depth=1",
         "--epub-cover-image", str(ASSETS / "cover.jpg"), "--css", str(WEB / "epub.css"),
         "--no-highlight", *epub_metadata(kindle)],
        input=book_markdown(kindle), text=True, check=True,
    )
    if kindle:
        strip_cover_page(out)
    return out


def strip_cover_page(path):
    """KDP: declare the cover image in the OPF only, with no separate HTML cover page."""
    with zipfile.ZipFile(path) as z:
        files = {n: z.read(n) for n in z.namelist()}
    cover_pages = [n for n in files if n.endswith("cover.xhtml")]
    for name in cover_pages:
        del files[name]
    for name in list(files):
        if not name.endswith((".opf", ".xhtml", ".ncx")):
            continue
        text = files[name].decode("utf-8")
        text = re.sub(r'\s*<item [^>]*href="[^"]*cover\.xhtml"[^>]*/>', "", text)
        text = re.sub(r'\s*<itemref idref="cover_xhtml"[^>]*/>', "", text)
        text = re.sub(r'\s*<reference [^>]*href="[^"]*cover\.xhtml"[^>]*/>', "", text)
        text = re.sub(r'\s*<li>\s*<a [^>]*href="[^"]*cover\.xhtml"[^>]*>[^<]*</a>\s*</li>', "", text)
        files[name] = text.encode("utf-8")
    with zipfile.ZipFile(path, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), files.pop("mimetype"), compress_type=zipfile.ZIP_STORED)
        for name, data in files.items():
            z.writestr(name, data, compress_type=zipfile.ZIP_DEFLATED)


def build_pdf():
    from weasyprint import HTML

    body = pandoc(book_markdown(kindle=False), "-t", "html5", "--no-highlight")
    titles = [heading(c.read_text(encoding="utf-8")) for c in CHAPTERS]
    toc = "\n".join(
        f'<li><a href="{build_manual.anchor(t)}">{html.escape(t)}</a></li>' for t in titles
    )
    document = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{TITLE}: {SUBTITLE}</title>
<meta name="author" content="{AUTHOR}"><meta name="description" content="{html.escape(DESCRIPTION)}">
<link rel="stylesheet" href="print.css"></head>
<body>
<section class="cover"><img src="../assets/cover.jpg" alt=""></section>
<nav class="toc"><p class="toc-title">Contents</p><ol>{toc}</ol></nav>
{body}
</body></html>"""
    out = SITE / "downloads/hard-target.pdf"
    HTML(string=document, base_url=str(WEB) + "/").write_pdf(out)
    return out


def main():
    if subprocess.run(
        [sys.executable, str(ROOT / "scripts/build_manual.py"), "--check"]
    ).returncode:
        print("MANUAL.md is stale. Run python3 scripts/build_manual.py first.", file=sys.stderr)
        return 1
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    build_site()
    free = build_epub(kindle=False)
    shutil.copy(free, SITE / "downloads/hard-target.epub")
    build_epub(kindle=True)
    shutil.copy(build_pdf(), DIST / "hard-target.pdf")
    print("Built site/, dist/hard-target.epub, dist/hard-target-kindle.epub and dist/hard-target.pdf")
    return 0


if __name__ == "__main__":
    sys.exit(main())
