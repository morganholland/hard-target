# 5. Harden the phone

Your phone holds your passkeys, your bank and your location history, so the two real risks are a thief who watched you type your passcode and apps that leak where you go.

**The case.** In January 2025, hackers breached location broker Gravy Analytics and leaked data drawn from thousands of ordinary apps, including games, dating and fitness apps. Most of those apps had no deal with the broker. The data came out of the ad auctions that run each time an ad loads. ([TechCrunch](https://techcrunch.com/2025/01/13/gravy-analytics-data-broker-breach-trove-of-location-data-threatens-privacy-millions/))

**Baseline: iPhone**

1. Settings > Face ID & Passcode: set a 6-digit or alphanumeric passcode, and turn on Stolen Device Protection with "Always".
2. Settings > Privacy & Security > Tracking: turn off "Allow Apps to Request to Track".
3. Settings > Privacy & Security > Location Services: set each app to "Never" or "While Using", and turn off Precise Location for everything except maps.
4. Settings > your name > iCloud: turn on Advanced Data Protection, after setting a recovery contact or recovery key.
5. Turn on automatic updates, including Rapid Security Responses.

**Baseline: Android**

1. Settings > Security & privacy: set a 6-digit or longer PIN, and turn on Theft Detection Lock and Remote Lock.
2. Settings > Privacy > Ads: delete the advertising ID.
3. Settings > Location > App permissions: set each app to "Don't allow" or "Only while using", and turn off "Use precise location".
4. Turn off Location History and Web & App Activity in your Google account, or set auto-delete to 3 months.
5. Install apps only from the Play Store. Keep Play Protect on.

**Both**

1. Delete every app you have not opened in 90 days. Fewer apps means fewer ad auctions carrying your location.
2. Hide notification previews on the lock screen, so codes cannot be read off a locked phone.
3. Cover your passcode in public the way you cover a PIN at a cash machine.

**Elevated**

1. Use Face ID or fingerprint in public so the passcode is rarely typed.
2. Review which apps can read contacts, photos, microphone and Bluetooth. Remove any that do not obviously need it.
3. Reboot weekly. Some spyware does not survive a restart.

**High-risk**

1. iPhone: turn on Lockdown Mode. Android 16: turn on Advanced Protection. Both trade convenience for a much smaller attack surface. ([EFF on Android](https://www.eff.org/deeplinks/2025/06/googles-advanced-protection-arrives-android-should-you-use-it), [Apple](https://support.apple.com/en-al/guide/platform-support/supd3139bab8/web))
2. Power the phone fully off before any situation where it may be taken from you. A phone that has not been unlocked since boot is far harder to extract.

**Agent prompt:** P6 (phone audit coach).
