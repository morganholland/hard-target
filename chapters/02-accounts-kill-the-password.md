# 2. Accounts: kill the password

Passkeys resist phishing and password reuse. Start with the email or device account that can reset your other accounts.

**The case.** In October 2026, FIDO estimated that seven billion passkeys were in use worldwide. Microsoft began enabling passkeys for eligible Entra users with SMS or voice authentication in September 2026. It scheduled the retirement of Microsoft-provided SMS and voice delivery for most in-scope users for February 2027, and for Global Administrators and external users for July 2027. These dates concern work identities. [FIDO estimate](https://fidoalliance.org/7-billion-passkeys-and-counting-the-next-chapter-of-passwordless-authentication/) · [Microsoft rollout](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement)

**Baseline**

1. Pick one password manager and use only it: [1Password](https://1password.com), [Bitwarden](https://bitwarden.com), or the one built into Apple or Google.
2. Where the manager uses a master passphrase, choose a long, unique one. Keep its recovery materials somewhere private that you could reach without your device.
3. Keep your trusted session open. Add a passkey to an important account, then verify a fresh sign-in in another browser session.
4. Set up and verify a recovery method you could use without that phone. Where the provider offers codes, reveal and save them privately, then store them offline in a safe place you control.
5. Once both checks pass, consider removing an optional SMS fallback. Keep it if it is required or is still your only working way back in.
6. Where a passkey is unavailable, use a unique password and the strongest second factor the provider supports. Keep access to a replacement factor before retiring the old one.
7. Check [Have I Been Pwned](https://haveibeenpwned.com) and change any password that appears in a breach.

**Elevated**

1. Choose two compatible hardware security keys. Keep the spare separately somewhere you can reach if the first one is lost. [YubiKey models](https://www.yubico.com/products/yubikey-5-overview/)
2. Register both on email, your password manager, your registrar and any financial account that accepts them.
3. For Google's [Advanced Protection Program](https://landing.google.com/advancedprotection/), register and test a separately stored backup key or passkey. Members cannot download backup codes. [Google recovery guidance](https://support.google.com/accounts/answer/7539956) · [Backup-code availability](https://support.google.com/accounts/answer/1187538?hl=en)
4. Review signed-in devices and third-party app access on every crown-jewel account. Remove anything you do not recognise.

**High-risk**

1. For accounts exposed to targeted phishing, consider hardware keys. Test both keys and the provider’s recovery procedure before removing an existing sign-in method. Losing all trusted devices and keys can permanently lock an Apple user out. [Apple security keys](https://support.apple.com/en-us/102637)
2. Keep a separate email address, known to nobody, purely for account recovery.

**Do not.** Do not approve a sign-in prompt you did not start. Do not read a code to anyone who called you. No real support agent needs it.

**Agent prompts:** [P1](../prompts/P1-account-inventory.md) (account inventory), [P2](../prompts/P2-passkey-upgrade-run.md) (passkey upgrade run).
