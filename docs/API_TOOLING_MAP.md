# API and Tooling Map

## Script generation

Options:
- OpenAI Responses API
- Anthropic Messages API
- local LLM for cheaper variants

Use for:
- hooks
- scripts
- captions
- image/video prompts
- post copy
- trend adaptations

## Voice

Options:
- ElevenLabs: premium cloned voice, character voices.
- OpenAI TTS: simple high-quality narration.
- MiniMax / Fish Audio / PlayHT / Cartesia: benchmark for price and quality.
- Real Harto recordings: best authenticity for hero content.

Use voice presets:
- narrator_curator
- lucia
- kamau
- noura_sfx_or_chirps
- harto_critic

## Avatar / host

Options:
- real Harto vertical clip library + automated overlays
- HeyGen for avatar/lip-sync
- Runway/Luma/Kling/Pika for scene/b-roll

Rule: do not publish raw corporate avatar output. Always wrap with Exquisite templates, captions, flowers, gallery UI, and world b-roll.

## Image and b-roll generation

Options:
- Midjourney for style exploration
- FLUX / FAL / Replicate for automated stills
- Runway / Luma / Kling / Pika / Veo-like tools for motion clips

Use for:
- semi-pixel cafés
- gallery scenes
- Noura reactions
- wallet gallery rooms
- city locations

## Rendering

Options:
- Remotion for programmatic 9:16 videos
- HTML/CSS templates + Playwright screenshots/video
- ffmpeg for assembly and subtitles
- CapCut/Premiere for manual pilots only

## Queue / database

Options:
- Airtable: best simple content pipeline.
- Notion: editorial board.
- Google Sheets: easy collaboration.
- Local JSON/CSV for MVP.

## Scheduling / publishing

Options:
- YouTube Data API for Shorts
- TikTok Content Posting API if approved
- Instagram Graph API for Reels if account supports it
- Buffer/Later/Metricool/Hypefury-style schedulers if direct APIs are annoying

## Analytics feedback

Track:
- hook
- series
- duration
- watch time
- completion rate
- saves
- shares
- comments
- profile clicks
- website clicks
- follows

Feed winners back into `data/trend_library.csv` and `data/content_formats.json`.
