# Plan: web, PDF, EPUB and Kindle editions

## Status

- **Done:** decisions agreed (below).
- **Next:** build script, tests, cover, CI deploy.
- **Owed by Morgan:** see [OWED.md](../OWED.md).

## Decisions (agreed 18 November 2026)

1. The repo becomes public, and the site is served by GitHub Pages from a GitHub Actions build.
2. License: CC BY-NC 4.0.
3. Kindle: KDP without KDP Select, list price $2.99 (70% royalty band).
4. Author: Morgan Holland.
5. Cover: original typographic design, 1600 × 2560 JPEG.
6. One toolchain: pandoc for HTML and EPUB, WeasyPrint for PDF, run by `scripts/build_editions.py` locally and in CI.

## Requirements

Each requirement maps to a check in `scripts/test_editions.py`, which runs against the built `site/` and `dist/` folders.

- **R1 Site pages.** `site/` has an index page and one HTML page per chapter (0 to 16), plus a sources page.
- **R2 Site navigation.** Every chapter page links to the contents page and to the previous and next chapters.
- **R3 Site links.** Every internal link and fragment on the site resolves. Links to prompt files point at the matching section of the chapter 15 page.
- **R4 Prompt copy.** Every paste-ready block on the site is a `<pre>` the reader can select. A copy button is added by script, and the page works without it.
- **R5 Downloads.** The index links to the PDF and the free EPUB, and both files exist in `site/downloads/`.
- **R6 PDF.** Letter size, a bookmarked outline with one entry per chapter, and no line of a prompt block running past the page edge.
- **R7 EPUB.** `dist/hard-target.epub` passes epubcheck with no errors and has one navigation entry per chapter.
- **R8 Kindle EPUB.** `dist/hard-target-kindle.epub` passes epubcheck with no errors, declares its cover with `properties="cover-image"`, has no separate HTML cover page, and carries title, author, language, date and description metadata.
- **R9 Cover.** `assets/cover.jpg` is a 1600 × 2560 RGB JPEG.
- **R10 KDP kit.** `kdp/` holds the listing text (description, keywords, categories, price, AI disclosure answer) used on the upload page.
- **R11 CI.** Pull requests build every edition and run the tests. Pushes to `main` also deploy `site/` to GitHub Pages and keep the Kindle EPUB as a private workflow artifact.
- **R12 License.** `LICENSE.md` states CC BY-NC 4.0, and every edition's copyright page says so.
