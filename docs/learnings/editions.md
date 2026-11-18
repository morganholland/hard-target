# Building the editions

- Read chapter files with pandoc's `gfm` reader. Its heading IDs match GitHub's, so the anchors `build_manual.py` writes into MANUAL.md also work in the PDF and both EPUBs.
- The `gfm` reader ignores `{.class}` heading attributes and prints them as text. Target headings by their generated ID in CSS instead.
- KDP wants the cover declared in the OPF with `properties="cover-image"` and no separate HTML cover page. Pandoc always adds `cover.xhtml`, so the Kindle build removes it from the manifest, spine, guide and nav landmarks. Missing the nav landmark is an epubcheck error.
- Task-list checkboxes render as `<input>` in EPUB, which many readers draw badly. The book editions turn them into plain bullets.
- WeasyPrint makes PDF bookmarks from `h1` and `h2`, and `target-counter()` fills in contents page numbers. Keep the cover and contents out of `h1` so the outline starts at chapter 0.
- The website loads no fonts, scripts or images from other hosts. That matters for a privacy manual, and keeps the site working offline.
- Claude sessions cannot change repository settings, including visibility and the Pages source. Ask the owner to flip those before the first deploy, or the first `main` deploy fails.
