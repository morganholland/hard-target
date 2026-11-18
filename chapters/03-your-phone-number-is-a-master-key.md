# 3. Your phone number is a master key

Whoever controls your number receives your text codes and password resets, so lock the number at the carrier and then stop depending on it.

**The case.** In a SIM swap, a criminal talks or bribes a carrier employee into moving your number to their SIM. Your phone goes dead, and their phone starts receiving your bank codes. All three big US carriers now offer free locks, and most customers have never switched them on. ([TechCrunch](https://techcrunch.com/2025/07/09/how-to-protect-your-cell-phone-number-from-sim-swap-attacks/))

**Baseline: carrier locks**

| Carrier | Blocks SIM changes | Blocks transfers to another carrier |
| --- | --- | --- |
| Verizon | SIM Protection | Number Lock |
| T-Mobile | SIM Protection | Port Out Protection |
| AT&T | Wireless Account Lock (covers both) | Wireless Account Lock |

Check the scope, required role, and notification recipients before changing anything. AT&T Wireless Account Lock works in the AT&T app for users with primary or secondary access. It covers the entire account. Switching it on or off emails the primary account holder and texts every active wireless line. [AT&T instructions](https://lsreg.att.com/support/article/wireless/000102016)

1. On other carriers, verify which protections apply by line and enable them only for lines you are authorised to manage. If notifications could put someone at risk, leave the settings alone until you have a safe plan.
2. Set a carrier account PIN that is not a birthday, and store it in your password manager.
3. For email and banking, test a new sign-in and independent recovery method before retiring optional SMS authentication.
4. A device SIM PIN protects the SIM or eSIM and is separate from the carrier account PIN. If the existing SIM PIN or unlock code (PUK) is unknown, stop and contact the carrier. Repeated guesses can permanently block the SIM. [Apple SIM PIN guide](https://support.apple.com/en-us/118228)

**Elevated**

1. Get a second number, from Google Voice or a second eSIM, and give that one to shops, apps and forms. Keep your real number for people.
2. Use [Signal](https://signal.org) with a username, and hide your phone number in its privacy settings.
3. Ask your bank which accounts still fall back to SMS, and whether a hardware key or app-only approval is available.

**High-risk**

1. Put financial accounts on a number that exists only for that purpose and is never given to a human.
2. Consider a carrier that requires in-person or multi-step verification for any SIM change.

**Warning sign.** An unexpected loss of service can signal a SIM swap. Contact your carrier from another phone if you suspect one. See [chapter 14](14-when-you-get-hit.md).

**Agent prompt:** [P3](../prompts/P3-carrier-lock-walk-through.md) (carrier lock walk-through).
