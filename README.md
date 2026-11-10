# N3mak — AI business agent on Telegram

N3mak is a Telegram agent that does three jobs for a small business, with no dashboard and no onboarding call.

## What it does

1. **Exposure check** — `/dive <company or domain>` searches published ransomware leak-site victims and returns the group, date and country when there is a match.
2. **Website dossier** — `/blue <site>` reports the detected stack (Shopify, WordPress, Salla, Next.js, payment providers, pixels) and lists the gaps: no instant reply channel, no FAQ, no self-service booking, no instant payment, no conversion tracking. Each gap carries a price estimate and a readiness score.
3. **Instant quoting** — `/quote` returns a fixed price with an order id and a payment address, and verifies the transfer automatically.

## Pricing

| Item | Price |
| --- | --- |
| Exposure report | 99 USD |
| Website dossier | 149 USD |
| Both for one company | 229 USD |
| Instant reply assistant implementation | from 900 USD |
| Content and publishing automation | from 900 USD |
| System integration and dashboard | from 3000 USD |
| Monthly maintenance | 200 USD / service |

Report purchases are collected inside Telegram with Telegram Stars. Service engagements are quoted with an order id and paid by USDC.

## Distribution

`/outlets` returns 23 verified publishing and sales channels, grouped as launch, freelance, classifieds, b2b and bot directories.

## Engineering notes

State lives in Neon Postgres, because the free hosting tier wipes local disk on every restart. The agent keeps itself awake with a self-ping every nine minutes, and republishes from a database-backed queue every six hours.

## Links

- Bot: https://t.me/N3mak_bot
- Product pages: https://namak7678.github.io/n3mak-services/tools/
- Sample report: https://namak7678.github.io/n3mak-services/tools/sample.html
