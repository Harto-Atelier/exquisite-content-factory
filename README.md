# Exquisite World Lore + Content Factory

A public canon and content-generation system for Exquisite World: the long-term story bible, character/world registries, website-readable lore data, and daily short-form story, brand, and utility video tooling around Lucía, Kamau, and Noura.

This repo is intended to be the source of truth that the main website/app can read from, and that the public can browse as the living archive of Exquisite World.

Goal: produce a structured daily batch of 30 short videos:

- 15 story / brand / worldbuilding videos
- 15 utility / website / onboarding videos

The system treats the website as part of the story: connecting a wallet becomes "presenting your wallet", the claim flow becomes the Claim Kiosk, the leaderboard becomes the Leaderboard Tower, and referrals become invitations into the room.

## Current status

This repo is the first foundation: world bible, content plan, prompt templates, API/tooling map, schemas, and a local script generator that creates a daily content queue from reusable formats.

It does not call paid APIs by default. API integrations are documented and stubbed so secrets can be added later through `.env` or GitHub Actions secrets.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
exq-content generate --date 2026-06-28 --count-story 15 --count-utility 15 --out data/daily_queue_2026-06-28.json
```

Or without installing:

```bash
python3 scripts/generate_daily_queue.py --date 2026-06-28 --count-story 15 --count-utility 15
```

## Repo map

Canon / lore:

- `lore/00-start-here/README.md` — how to use this as the public canon repo.
- `lore/01-story-bible/STORY_BIBLE.md` — 10-year story bible and emotional architecture.
- `lore/02-characters/` — character records for Lucía, Kamau, Noura, Agents, and Curators.
- `lore/03-world/` — locations and rituals registry.
- `lore/04-timeline/` — 10-year era structure.
- `lore/05-episodes/` — episode formats and Season 1 structure.
- `lore/06-style-guides/` — voice, tone, and visual language.
- `lore/07-website-data/exquisite-world.json` — machine-readable lore for website/app import.
- `lore/08-canon-registry/canon-log.md` — canonical change log.
- `schemas/exquisite-world.schema.json` — JSON schema for website-readable data.

Legacy/planning docs:

- `docs/WORLD_BIBLE.md` — original characters, locations, visual rules, tone, language.
- `docs/WEB_LORE.md` — English website lore for Lucía, Kamau, Noura, the pixel garden, Agents, wallet, and invitation.
- `docs/CONTENT_SYSTEM.md` — daily system, formats, trend-jacking rules, production pipeline.
- `docs/AUTOMATION_PLAN.md` — phased build plan and automation stack.
- `docs/API_TOOLING_MAP.md` — APIs/tools for script, voice, image, video, render, scheduling, analytics.
- `docs/WEBSITE_UTILITY_STORIES.md` — maps website actions into story rituals.
- `data/content_formats.json` — repeatable story/utility formats.
- `data/trend_library.csv` — trend structures to adapt into Exquisite format.
- `data/pilot_topics.json` — first story and utility topics.
- `prompts/` — prompt templates for script, image, video, voice, captions.
- `src/exquisite_content_factory/` — Python package for generating queues/scripts.
- `scripts/` — runnable helper scripts.
- `templates/` — future Remotion/HTML/ffmpeg templates.
- `renders/` — ignored output folder for generated media.

## Core creative rule

Universal human moment + Exquisite World setting + artist/curator interpretation + small emotional twist + soft website/action connection.

Example:

> Lucía wanted iced matcha. Kamau remembered the order. Noura found the hidden painting. The Curator wrote: "A ritual repeated with love becomes a doorway." Present your wallet.

## Main trio

- Lucía — emotional, intuitive, sees meaning before others do.
- Kamau — warm, playful, loyal, treats the world like a quest map.
- Noura — small chicken companion, comic/mystical mascot, often chooses the right artwork or button.

Tagline candidates:

- Two lovers, one chicken, and a city that curates every feeling.
- Every love story deserves a curator.
- Lucía and Kamau came for art. Noura found the door.
