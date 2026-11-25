# Zapier App Directory Scraper & Unofficial API (Python, Node.js, MCP)

[Run Zapier App Directory Scraper on Apify](https://apify.com/evpp/zapier-app-directory) to export Zapier App Directory data as clean JSON, CSV, Excel, or an API feed. This repository is a developer quick-start kit with working Python and Node.js clients, an MCP configuration, a real sample dataset, and an n8n automation template.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-orange)](https://apify.com/evpp/zapier-app-directory)

## Why use this Zapier App Directory scraper?

- Export Zapier App Directory data without building or maintaining a custom scraper
- Get flat, schema documented JSON ready for analytics, lead generation, market research, and AI agents
- Run manually, on a schedule, through the Apify API, or through MCP compatible AI tools
- Use the included 25+ row sample dataset to prototype before running the live Actor

Built for SaaS partnership/biz-dev teams, integration market researchers, VCs tracking automation ecosystem.

## Quick start on Apify

Open [https://apify.com/evpp/zapier-app-directory](https://apify.com/evpp/zapier-app-directory) and use this input:

```json
{
  "category": "sales-crm",
  "maxItems": 15
}
```

## Python

```bash
pip install -r requirements.txt
export APIFY_TOKEN=your_apify_token
python python/run.py
```

On Windows PowerShell, use `$env:APIFY_TOKEN="your_apify_token"` instead of `export`.

## Node.js

```bash
npm install
export APIFY_TOKEN=your_apify_token
node node/run.mjs
```

## MCP and AI agents

Add the hosted Apify MCP server from `mcp-config.json` to your MCP client:

```json
{
  "mcpServers": {
    "apify": {
      "type": "http",
      "url": "https://mcp.apify.com/?tools=evpp/zapier-app-directory"
    }
  }
}
```

Then ask your agent to run `evpp/zapier-app-directory`, inspect the output schema, or export the latest dataset. The direct MCP URL is `https://mcp.apify.com/?tools=evpp/zapier-app-directory`.

## n8n automation

Import `n8n-workflow.json` into n8n, select your Apify credential, replace the webhook placeholder, and activate the schedule. The workflow runs the Actor every morning and posts fresh dataset items to your webhook.

## Output schema

| Field | Type | Description |
|---|---|---|
| `id` | integer | Internal Zapier app ID |
| `title` | string | App name as shown in the Zapier directory |
| `slug` | string | URL-friendly app identifier used across zapier.com |
| `url` | string | Zapier integrations page for the app |
| `description` | string | Short app description (trimmed to ~300 characters) |
| `categories` | string[] | Category titles the app is listed under |
| `categorySlugs` | string[] | Category slugs the app is listed under (usable as the category input) |
| `domain` | string | Vendor website domain derived from the app's external URL |
| `apiDocsUrl` | string | Link to the app's public API documentation |
| `imageUrl` | string | App logo image (128x128 CDN URL) |
| `ageInDays` | integer | How many days the app has been listed on Zapier |
| `siteUrl` | string | Vendor website URL registered for the app |
| `zapUsageCount` | integer | Number of Zaps using this app (Zapier usage counter) |
| `popularity` | integer | Zapier popularity rank of the app (1 = most popular) |
| `isPremium` | boolean | Whether the app requires a paid Zapier plan |
| `isBeta` | boolean | Whether the app integration is flagged as beta |
| `isFeatured` | boolean | Whether the app is featured by Zapier |
| `isUpcoming` | boolean | Whether the integration is announced but not yet launched |
| `hashtag` | string | Marketing hashtag Zapier assigns to the app |
| `primaryColor` | string | Brand primary color hex code (no leading #) |

## Real sample output

The first sanitized row from the included sample dataset:

```json
{
  "id": 11898,
  "title": "Apollo",
  "slug": "apollo",
  "url": "https://zapier.com/apps/apollo/integrations",
  "description": "Apollo is a unified engagement platform that is the foundation for your entire end-to-end sales strategy. Teams get access to a database of over 200 million contacts, as well as a host of different engagement and analytics tools.",
  "categories": [
    "Sales & CRM"
  ],
  "categorySlugs": [
    "sales-crm"
  ],
  "domain": "apollo.io",
  "apiDocsUrl": "https://apolloio.github.io/apollo-api-docs/?shell#introduction",
  "imageUrl": "https://cdn.zapier.com/img/services/f182ae680fb17b2ec9047a6e4014a99f.png?size=128x128",
  "ageInDays": 2066,
  "siteUrl": "https://www.apollo.io/",
  "zapUsageCount": 1663,
  "popularity": 177,
  "isPremium": false,
  "isBeta": false,
  "isFeatured": false,
  "isUpcoming": false,
  "hashtag": "#Apollo",
  "primaryColor": "242D3E"
}
```

## Files in this kit

| File | Purpose |
|---|---|
| `python/run.py` | Working Python Apify API example |
| `node/run.mjs` | Working Node.js Apify API example |
| `mcp-config.json` | MCP server configuration for AI agents |
| `sample-output.json` | First five sanitized sample rows |
| `dataset-snapshot.csv` | 25+ row evaluation snapshot |
| `DATASET_CARD.md` | Dataset documentation and provenance |
| `n8n-workflow.json` | Scheduled n8n automation template |

## Fresh data

This repository contains a static evaluation sample. For current data, run the live Actor: https://apify.com/evpp/zapier-app-directory

## Responsible use

The Actor reads public data from `zapier.com`. Review the source site's terms and applicable privacy rules before production use.
