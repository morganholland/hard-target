"""Refresh the embedded prompt library and single-file edition. Use --check in CI."""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
PROMPTS = ROOT / "prompts"
LIBRARY = CHAPTERS / "15-agent-prompt-library.md"
RULES = PROMPTS / "00-RULES.md"
SOURCES = ROOT / "SOURCES.md"
MANUAL = ROOT / "MANUAL.md"


def heading(markdown):
    return markdown.splitlines()[0].removeprefix("# ")


def anchor(title):
    # These headings use ASCII words, numbers, spaces, and punctuation.
    return "#" + re.sub(r"[^\w -]", "", title.lower()).replace(" ", "-")


def prompt_block(path):
    matches = re.findall(r"^```\n[\s\S]*?^```$", path.read_text(encoding="utf-8"), flags=re.M)
    if len(matches) != 1:
        raise ValueError(f"Expected one paste-ready block in {path.name}")
    return matches[0]


def build_editions():
    prompt_files = sorted(
        PROMPTS.glob("P*-*.md"), key=lambda path: int(path.name[1:].split("-")[0])
    )
    intro, marker, _ = LIBRARY.read_text(encoding="utf-8").partition("\n## Shared rules\n")
    if not marker:
        raise ValueError("Missing 'Shared rules' heading in the prompt library")

    chapters = {path: path.read_text(encoding="utf-8") for path in sorted(CHAPTERS.glob("*.md"))}
    targets = {path: anchor(heading(content)) for path, content in chapters.items()}
    targets[RULES] = "#shared-rules"
    sections = [intro.rstrip(), "## Shared rules", prompt_block(RULES)]
    for path in prompt_files:
        title = heading(path.read_text(encoding="utf-8"))
        targets[path] = anchor(title)
        sections.extend(["## " + title, prompt_block(path)])
    library = "\n\n".join(sections) + "\n"
    chapters[LIBRARY] = library
    chapters[SOURCES] = SOURCES.read_text(encoding="utf-8")
    targets[SOURCES] = "#sources"

    manual = ["# Hard Target: The 2026 Field Manual for Digital Privacy"]
    for path, content in chapters.items():
        # Preserve paste-ready code verbatim. Rewrite prose links to sections
        # so a downloaded copy of MANUAL.md works without the rest of the repo.
        chunks = content.split("```")

        def local_link(match):
            destination = (path.parent / match[1]).resolve()
            return "](" + targets[destination] + ")"

        for index in range(0, len(chunks), 2):
            chunks[index] = re.sub(r"\]\(([^():#\s]+\.md)\)", local_link, chunks[index])
            # Demote every prose heading one level: chapter titles become ##.
            chunks[index] = re.sub(r"(?m)^(#{1,5}) ", r"#\1 ", chunks[index])
        manual.append("```".join(chunks).strip())
    return {LIBRARY: library, MANUAL: "\n\n".join(manual) + "\n"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report stale output without writing")
    args = parser.parse_args()
    changed = []
    for file, expected in build_editions().items():
        if not file.exists() or file.read_text(encoding="utf-8") != expected:
            changed.append(str(file.relative_to(ROOT)))
            if not args.check:
                file.write_text(expected, encoding="utf-8")
    if args.check and changed:
        print("Rebuild with python3 scripts/build_manual.py: " + ", ".join(changed), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
