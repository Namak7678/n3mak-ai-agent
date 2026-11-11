![Telegram](https://img.shields.io/badge/Telegram-%40N3mak__bot-22d3ee?style=flat-square)
![Status](https://img.shields.io/badge/status-live-22d3ee?style=flat-square)
![Pricing](https://img.shields.io/badge/reports-99%20%2F%20149%20USD-ff6a3d?style=flat-square)
![State](https://img.shields.io/badge/state-Neon%20Postgres-34d399?style=flat-square)

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

## Client area and agency feed

- Client portal: https://namak7678.github.io/n3mak-pay/portal/
- Generated service agreement: https://namak7678.github.io/n3mak-pay/contract/?id=NMKTEST
- - Exposure index and press page: https://namak7678.github.io/n3mak-radar/press.html
Radar feed by country: https://namak7678.github.io/n3mak-pay/radar/
- Agency brief: 900 Telegram Stars a month, `/subscribe` in the bot

## Links

- Bot: https://t.me/N3mak_bot?start=gh_readme
- Product pages: https://namak7678.github.io/n3mak-services/tools/
- Sample report: https://namak7678.github.io/n3mak-services/tools/sample.html


## Try it in one line

Open https://t.me/N3mak_bot?start=gh_readme and type `/blue yourdomain.com`.

## For maintainers of directories

The agent runs 24/7 on a single service, keeps its own state in Postgres, and pays for itself with Telegram Stars. If you list tools for small businesses, this one needs no signup and no dashboard.
