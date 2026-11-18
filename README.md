# Hard Target

**A 2026 field manual for digital privacy, with paste-ready prompts that let an AI agent do the legwork.**

You cannot be invisible in 2026, but you can be a hard target: expensive to scam, slow to find, and quick to recover. Most chapters open with a real, sourced case, then gives the moves ranked by impact across three tiers: Baseline, Elevated and High-risk.

> If someone may be monitoring your device or shares your accounts, use a device they cannot reach and read the [safety note](chapters/00-start-here.md) before changing anything. If money just moved or your number was taken over, go straight to [incident response](chapters/14-when-you-get-hit.md).

- Read it online: [morganholland.github.io/hard-target](https://morganholland.github.io/hard-target/), chapter by chapter
- Download it: [PDF](https://morganholland.github.io/hard-target/downloads/hard-target.pdf) or [EPUB](https://morganholland.github.io/hard-target/downloads/hard-target.epub)
- Read it in one file here: [MANUAL.md](MANUAL.md)
- Short on time? Do the [90-minute quick start](chapters/00-start-here.md).
- Want an agent to do it? Start with [the rules](prompts/00-RULES.md), then [P0](prompts/P0-build-my-plan.md).

## Chapters

| # | Chapter |
| --- | --- |
| 0 | [Start here](chapters/00-start-here.md) |
| 1 | [What changed since 2017](chapters/01-what-changed-since-2017.md) |
| 2 | [Accounts: kill the password](chapters/02-accounts-kill-the-password.md) |
| 3 | [Your phone number is a master key](chapters/03-your-phone-number-is-a-master-key.md) |
| 4 | [Email and identity compartments](chapters/04-email-and-identity-compartments.md) |
| 5 | [Harden the phone](chapters/05-harden-the-phone.md) |
| 6 | [Browser, search and network](chapters/06-browser-search-and-network.md) |
| 7 | [Data brokers: take yourself off the shelf](chapters/07-data-brokers-take-yourself-off-the-shelf.md) |
| 8 | [Money](chapters/08-money.md) |
| 9 | [AI impersonation](chapters/09-ai-impersonation.md) |
| 10 | [What you tell AI](chapters/10-what-you-tell-ai.md) |
| 11 | [Home](chapters/11-home.md) |
| 12 | [Car and the physical world](chapters/12-car-and-the-physical-world.md) |
| 13 | [Family and kids](chapters/13-family-and-kids.md) |
| 14 | [When you get hit](chapters/14-when-you-get-hit.md) |
| 15 | [Agent prompt library](chapters/15-agent-prompt-library.md) |
|  | [Upkeep](chapters/16-upkeep.md) |

## Agent prompts

Paste [RULES](prompts/00-RULES.md) first, then one prompt. The rules keep you in control: you take over the screen before anything secret appears, the agent treats web pages as information rather than instructions, and it asks before every submit, send, delete or purchase. If a tool cannot pause screen capture while you take over, follow its directions in your own browser instead. P14 runs only on a schedule you approve, with results sent somewhere private.

| Prompt | What it does | Needs |
| --- | --- | --- |
| P0 | [Build my plan](prompts/P0-build-my-plan.md) | chat |
| P1 | [Account inventory](prompts/P1-account-inventory.md) | email read access |
| P2 | [Passkey upgrade run](prompts/P2-passkey-upgrade-run.md) | browser agent |
| P3 | [Carrier lock walk-through](prompts/P3-carrier-lock-walk-through.md) | browser or chat coach, carrier app where required |
| P4 | [Data-broker opt-out sweep](prompts/P4-data-broker-opt-out-sweep.md) | browser agent |
| P5 | [Credit freeze concierge](prompts/P5-credit-freeze-concierge.md) | browser agent |
| P6 | [Phone audit coach](prompts/P6-phone-audit-coach.md) | chat |
| P7 | [Review and close selected accounts](prompts/P7-dormant-account-purge.md) | browser agent |
| P8 | [Incident triage](prompts/P8-incident-triage.md) | chat |
| P9 | [Family protocol and scam drill builder](prompts/P9-family-protocol-and-scam-drill-builder.md) | chat |
| P10 | [Car data check](prompts/P10-car-data-check.md) | browser agent |
| P11 | [The stranger test](prompts/P11-the-stranger-test.md) | browser agent or chat with search |
| P12 | [Big-platform privacy sweep](prompts/P12-big-platform-privacy-sweep.md) | browser agent |
| P13 | [AI account hygiene check](prompts/P13-ai-account-hygiene-check.md) | browser agent |
| P14 | [Quarterly re-check](prompts/P14-quarterly-re-check.md) | private scheduler or manual reminder |

## Notes

- Facts and cases were checked on 18 November 2026. See [SOURCES.md](SOURCES.md).
- Settings paths and menu labels change often. If one has moved, search the app's settings for the feature name.
- This is general security guidance, not legal or financial advice.
- Licensed under [CC BY-NC 4.0](LICENSE.md): share and adapt it freely, but not for sale.

## Editing the manual

Edit the standalone chapters and prompt files first. Run `python3 scripts/build_manual.py` to refresh the embedded prompts and single-file edition. Run `python3 scripts/build_manual.py --check` to check that the copies match.

To build the other editions, install pandoc, then `pip install weasyprint pypdf epubcheck`, and run `python3 scripts/build_editions.py` followed by `python3 scripts/test_editions.py`. The website lands in `site/`, and the book files in `dist/`. Every push to `main` rebuilds the site on GitHub Pages. The Kindle EPUB for KDP is kept as the `editions` workflow artifact on each `main` build, with its listing text in [kdp/listing.md](kdp/listing.md). The cover comes from `scripts/make_cover.py`.
