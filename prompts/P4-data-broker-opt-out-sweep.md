# P4. Data-broker opt-out sweep

**Needs:** browser agent

Paste [RULES](00-RULES.md) first, then this. Fill in anything in [BRACKETS].

```
Remove my own listings from people-search sites. My details, to be used only for finding and removing my own records: name [FULL NAME], other names used [ALIASES], current city and state [CITY, STATE], previous cities [LIST], age [AGE].

Sites: Spokeo, Whitepages, BeenVerified, Intelius, PeopleFinders, Radaris, TruePeopleSearch, FastPeopleSearch, Nuwber, MyLife, Instant Checkmate, TruthFinder, USPhonebook, ClustrMaps, That's Them.

For each site: search for me. If there is no match, log "not listed". If there is a match, show it to me to confirm it is me, then open the site's own opt-out or "do not sell" page and fill the form with the minimum fields. Ask before submitting. Do not create an account, do not pay, do not give a phone number. If a confirmation email is required, tell me and I will click it myself.

Do not look up, record or report on anyone else. If relatives appear on my listing, note only that the listing exposes relatives.

Finish with the log table and a re-check date 30 days from today.
```
