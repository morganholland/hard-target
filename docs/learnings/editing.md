# Editing the manual

- Safety caveats belong in one visible callout, not in every step. Readers skim the first line of each checklist item, so lead with the action verb and put the condition in the second sentence.
- Keep each instruction in one home. Payment-fraud routing lives in chapter 14 and P8; other chapters link there. Duplicated instructions drift, and the build script only keeps the prompts and MANUAL.md in sync.
- Date-specific notes (service outages, deadlines) go stale fast. Prefer the recurring pattern ("offline mid-November to mid-January") and link the official page.
- Chapter files use `#` for the title and `##` for sections. The build demotes every heading by one level inside MANUAL.md, so do not skip levels.
- After any edit to a chapter or prompt, run `python3 scripts/build_manual.py`. CI runs `--check` and fails if MANUAL.md or the prompt library is stale.
