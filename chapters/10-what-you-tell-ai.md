# 10. What you tell AI

A chatbot is a third party that stores what you type, and an agent is a third party that can act as you. Decide what each one is allowed to know and do before you start.

**The case.** Through 2026, researchers repeatedly hijacked AI browser agents with instructions hidden inside ordinary web pages, emails and posts. The agent read the page, obeyed the hidden text, and acted with the user's own logged-in access. In December 2025 OpenAI said this class of attack, prompt injection, may never be fully eliminated. ([Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-research-note-agentic-blabbering-ai-browser-phishing-202/))

**Baseline: chatbots**

1. Check whether your plan lets you turn off use of conversations for model training. Check the separate controls for visible history, memory, and retention.

| Assistant | Where the switch is |
| --- | --- |
| ChatGPT | Settings > Data Controls > "Improve the model for everyone" |
| Claude | Settings > Privacy > "Help improve Claude" |
| Gemini | Gemini Apps Activity > Keep Activity |

Labels move. Search the settings for "training" or "improve". ([Guide, October 2026](https://www.xray.tech/post/how-to-stop-chatgpt-claude-gemini-training-on-your-data))

2. For sensitive questions, share only what is necessary. Temporary mode can keep a chat out of visible history while the provider still retains it. Google says Gemini temporary chats and chats with Keep Activity off are retained for 72 hours. [Gemini Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en)
3. Never paste passwords, recovery codes, seed phrases, full card numbers or Social Security numbers into any chat.
4. Inspect memory entries privately in the provider’s own settings. Choose there which ones to remove.
5. Strip names and identifying details from other people's information before you paste it.
6. Remember that chat logs can be requested in a lawsuit or investigation. They are not privileged like a conversation with your lawyer.

**Baseline: agents and connectors**

1. Connect only the accounts a task needs. Disconnect them when the task is done.
2. Run browser agents in a separate browser profile that is signed in to nothing you would hate to lose.
3. Keep the agent in ask-before-acting mode for anything that sends, buys, deletes, submits a form or changes a setting.
4. Take private control on the screen **before** opening sign-in, recovery codes, or identity forms. Save or enter information privately and navigate away before returning control. If capture cannot be paused, use your own browser while the agent gives directions. [ChatGPT agent controls](https://help.openai.com/en/articles/11752874-chatgpt-agent)
5. Do not let an agent read your whole inbox and browse the open web in the same session. Untrusted content plus private data plus the ability to send is the dangerous combination.
6. Watch the first run of any new workflow from start to finish before you trust it unattended.

**Elevated**

1. Use a business or enterprise plan for work material. Those tiers exclude your data from training by contract.
2. Keep a short written list of what must never go into any AI tool: client secrets, unreleased financials, other people's health data.
3. Review the third-party apps, extensions and skills your assistants can call. Remove any you did not install on purpose.

**High-risk**

1. Run a local model on your own machine for anything that could identify a source or a protected person.

**Agent prompt:** [P13](../prompts/P13-ai-account-hygiene-check.md) (AI account hygiene check). All the agent prompts in [chapter 15](15-agent-prompt-library.md) are built on these rules.
