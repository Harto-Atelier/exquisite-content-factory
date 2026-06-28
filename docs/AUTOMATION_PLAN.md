# Automation Plan

## Phase 1 — Foundation

- World bible
- Content formats
- Trend library
- Prompt templates
- Daily queue schema
- Local generator that outputs 30 structured video briefs

## Phase 2 — Pilot batch

Create 10 videos manually/semi-automatically:

- 5 story videos
- 5 utility videos

Lock:
- visual style
- caption style
- voice style
- CTA language
- export specs

## Phase 3 — Batch generator

Pipeline:

structured input → script → voice → visuals/b-roll → captions → render → thumbnail → post copy → schedule

Recommended stack:

- Python for orchestration
- LLM API for scripts and prompts
- ElevenLabs / OpenAI / MiniMax / Fish Audio for voice
- HeyGen or real Harto clip library for host/avatar
- Runway / Kling / Luma / Pika / Veo-style tools for b-roll
- Remotion or HTML + ffmpeg for rendering
- Airtable / Notion / Google Sheets for content queue
- TikTok / YouTube / Instagram APIs or scheduler tools for publishing
- platform analytics export for feedback loop

## Phase 4 — Daily loop

Morning:
- collect trends
- generate 30 briefs
- approve hooks/scripts

Midday:
- generate voice, visuals, captions
- render drafts

Afternoon:
- approval pass
- schedule/publish

Next morning:
- analyze performance
- generate more of what worked

## Human approval gates

Human taste remains mandatory for:
- first 10 pilots
- character/world changes
- Harto face/voice use
- final output before public posting until the system is proven
- anything involving paid APIs at scale

## Secrets

Never commit API keys. Use `.env` locally and GitHub Actions secrets remotely.

Local `.env` candidates:

```bash
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
ELEVENLABS_API_KEY=
HEYGEN_API_KEY=
RUNWAY_API_KEY=
LUMA_API_KEY=
REPLICATE_API_TOKEN=
FAL_KEY=
AIRTABLE_API_KEY=
AIRTABLE_BASE_ID=
NOTION_TOKEN=
YOUTUBE_CLIENT_ID=
YOUTUBE_CLIENT_SECRET=
```
