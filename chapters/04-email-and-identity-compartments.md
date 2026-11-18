# 4. Email and identity compartments

Your email address is the username for your whole life, so stop handing the same one to everyone. Split it into compartments, and a breach in one stops there.

**The case.** National Public Data acknowledged a breach in 2024. A Senate inquiry recorded two different claims: one party described a release of 2.7 billion records, and a lawsuit cited a seller’s claim about 2.9 billion individuals. Neither figure establishes how many distinct people the release affected. Email aliases can limit reuse of an exposed login address across services. [Senate inquiry](https://www.grassley.senate.gov/imo/media/doc/grassley_to_jerico-national_public_data_-_national_public_data_hack.pdf)

**Baseline: three addresses**

| Address | Used for | Who knows it |
| --- | --- | --- |
| Vault | Banks, government, password manager, account recovery | Nobody. Never typed into a shop or newsletter. |
| Personal | Real people | Friends, family, colleagues |
| Public | Shopping, sign-ups, loyalty cards | Anyone. Assume it leaks. |

1. Create the vault address at a provider with strong sign-in, such as [Proton Mail](https://proton.me/mail) or a fresh Gmail with Advanced Protection.
2. Move bank, tax, broker and password-manager logins to the vault address over the next month.
3. Turn on a masked-email service for everything in the public bucket: Apple Hide My Email, [SimpleLogin](https://simplelogin.io), [addy.io](https://addy.io) or Fastmail masked email. One alias per site.
4. If an alias starts receiving spam, block the sender or review the alias. Before disabling or deleting it, change it at every service that uses it for login or recovery. Confirm delivery at the new address and test sign-in. If a dependency is unclear, keep the alias. [SimpleLogin guidance](https://simplelogin.io/docs/getting-started/delete-alias/)

**Elevated**

1. Give every service a different answer to "mother's maiden name" style questions. Generate nonsense and store it in the password manager.
2. Use a custom domain for personal mail, so you can change providers without changing address. Lock the domain with a hardware key and registrar lock.
3. Turn off automatic image loading in your mail app. Tracking pixels tell senders when and where you opened a message.
4. Use a mailing address that is not your home for registrations: a PO box or a virtual mailbox.

**High-risk**

1. Keep names apart, not just addresses. A project, a company and your household should not share a recovery phone, a payment card or a profile photo.

**Agent prompts:** [P1](../prompts/P1-account-inventory.md) (account inventory), [P7](../prompts/P7-dormant-account-purge.md) (review and close selected accounts).
