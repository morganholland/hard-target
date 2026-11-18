# 5. Harden the phone

Your phone holds your passkeys, your bank and your location history, so the two real risks are a thief who watched you type your passcode and apps that leak where you go.

**The case.** In January 2025, hackers breached location broker Gravy Analytics and leaked data drawn from thousands of ordinary apps, including games, dating and fitness apps. Most of those apps had no deal with the broker. The data came out of the ad auctions that run each time an ad loads. ([TechCrunch](https://techcrunch.com/2025/01/13/gravy-analytics-data-broker-breach-trove-of-location-data-threatens-privacy-millions/))

**Baseline: iPhone**

1. Settings > Face ID & Passcode: set a 6-digit or alphanumeric passcode, and turn on Stolen Device Protection with "Always".
2. Settings > Privacy & Security > Tracking: turn off "Allow Apps to Request to Track".
3. Settings > Privacy & Security > Location Services: set each app to "Never" or "While Using", and turn off Precise Location for everything except maps.
4. Where available, consider Advanced Data Protection under your iCloud settings after arranging and checking a recovery contact or recovery key. Apple says new UK users cannot enable it. If unavailable, skip it and record that status. [Apple UK guidance](https://support.apple.com/en-lk/122234)
5. Turn on automatic software updates. On iOS 26.1 or later, check Settings > Privacy & Security > Background Security Improvements. On older versions, follow the update controls available for that release. [Apple update guidance](https://support.apple.com/en-us/102657)

**Baseline: Android**

1. Settings > Security & privacy: set a 6-digit or longer PIN, and turn on Theft Detection Lock and Remote Lock.
2. Settings > Privacy > Ads: delete the advertising ID.
3. Settings > Location > App permissions: set each app to "Don't allow" or "Only while using", and turn off "Use precise location".
4. Turn off Location History and Web & App Activity in your Google account, or set auto-delete to 3 months.
5. Install apps only from the Play Store. Keep Play Protect on.

**Both**

1. Review rarely used apps. Keep authenticators, recovery tools, wallets, and apps with local files until you have backed up or transferred what you need and verified access separately. Some authenticator codes are stored only on the device. [Google Authenticator](https://support.google.com/accounts/answer/1066447?hl=en)
2. Hide notification previews on the lock screen, so codes cannot be read off a locked phone.
3. Cover your passcode in public the way you cover a PIN at a cash machine.

**Elevated**

1. Use Face ID or fingerprint in public so the passcode is rarely typed.
2. Review which apps can read contacts, photos, microphone and Bluetooth. Remove any that do not obviously need it.
3. Reboot weekly. Some spyware does not survive a restart.

**High-risk**

1. iPhone: turn on Lockdown Mode. Android 16: turn on Advanced Protection. Both trade convenience for a much smaller attack surface. ([EFF on Android](https://www.eff.org/deeplinks/2025/06/googles-advanced-protection-arrives-android-should-you-use-it), [Apple](https://support.apple.com/en-al/guide/platform-support/supd3139bab8/web))
2. Power the phone fully off before any situation where it may be taken from you. A phone that has not been unlocked since boot is far harder to extract.

**Agent prompt:** [P6](../prompts/P6-phone-audit-coach.md) (phone audit coach).
