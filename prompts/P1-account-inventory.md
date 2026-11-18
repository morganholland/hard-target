# P1. Account inventory

**Needs:** email read access

Paste [RULES](00-RULES.md) first, then paste the block below.

```
Use read-only inbox metadata to build a partial inventory of online accounts. Look for senders and subjects such as welcome, verification, password reset, receipt, subscription, and security alert. If your connector cannot restrict the returned data to the required metadata, give me a search I can run myself. Do not open messages or links or use the web.

For each service report first and last matching email, confidence in the match, and one of CROWN JEWEL (email, money, carrier, cloud, password manager, registrar), KEEP (I confirmed it), or REVIEW (default). Label the date “last matching email.” Mark the login address or access as unknown unless I confirm it. A quiet inbox tells you nothing about actual use, and the list will miss accounts. Never nominate an account for deletion or pass it automatically to P7.
```
