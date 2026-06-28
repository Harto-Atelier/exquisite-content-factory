from __future__ import annotations

import json
import random
from dataclasses import dataclass, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

STORY_HOOKS = [
    "Lucía bought the painting before Kamau could ask why.",
    "Kamau knew Lucía's matcha order. Noura knew the painting behind it.",
    "Noura chose the weird one.",
    "The hug changed the room.",
    "Kamau thought it was a website. Lucía knew it was a map.",
    "Noura was not allowed inside the museum.",
    "They never said 'I love you' in the gallery.",
    "Every morning, Noura waited for the city to choose.",
]

UTILITY_HOOKS = [
    "Your wallet is not a login. It is a gallery key.",
    "The Claim Kiosk only opens when the city recognizes you.",
    "The Leaderboard Tower grows every night.",
    "The Roulette Fountain chooses who the city notices today.",
    "A good invitation is architecture.",
    "The Trading Desk is where proposals become stories.",
    "The Ordinals Archive remembers every child and every shadow.",
]

CURATOR_NOTES = [
    "Taste often arrives wearing feathers.",
    "A ritual repeated with love becomes a doorway.",
    "The subject is not the image. The subject is memory.",
    "A good invitation is architecture.",
    "A ranking is just a garden that remembers participation.",
    "Declaration, no words.",
    "Some companions are not pets. They are provenance.",
]

@dataclass
class VideoBrief:
    id: str
    date: str
    kind: str
    series: str
    title: str
    hook: str
    duration_sec: int
    voiceover: str
    visual_beats: list[str]
    cta: str
    production_notes: list[str]


def load_formats() -> dict:
    return json.loads((ROOT / "data" / "content_formats.json").read_text())


def make_story(i: int, date: str, fmt: dict) -> VideoBrief:
    hook = STORY_HOOKS[i % len(STORY_HOOKS)]
    note = CURATOR_NOTES[i % len(CURATOR_NOTES)]
    title = f"{fmt['series']} #{i+1}: {hook.split('.')[0]}"
    voiceover = (
        f"{hook} Lucía stopped first. Kamau tried to understand the map. "
        f"Noura pecked once, like the answer was obvious. "
        f"The Curator wrote: '{note}' Enter the gallery."
    )
    return VideoBrief(
        id=f"{date}-story-{i+1:02d}",
        date=date,
        kind="story",
        series=fmt["series"],
        title=title,
        hook=hook,
        duration_sec=fmt.get("duration", 22),
        voiceover=voiceover,
        visual_beats=[
            "9:16 establishing shot of Exquisite World location",
            "Lucía and Kamau emotional micro-action",
            "Noura comic/magic discovery",
            "Curator note appears as museum label",
            "Soft CTA end card",
        ],
        cta="Enter the gallery.",
        production_notes=["Use semi-pixel colorful gallery/café/city style", "Keep captions short", "Noura reaction shot is the retention beat"],
    )


def make_utility(i: int, date: str, fmt: dict) -> VideoBrief:
    hook = UTILITY_HOOKS[i % len(UTILITY_HOOKS)]
    feature = fmt.get("feature", "website")
    cta = fmt.get("cta", "Present your wallet.")
    title = f"{fmt['series']} #{i+1}: {feature.replace('_', ' ').title()}"
    voiceover = (
        f"{hook} Kamau calls it a feature. Lucía calls it a room. "
        f"Noura pecks the right button. On the website, this means: {feature.replace('_', ' ')}. "
        f"{cta}"
    )
    return VideoBrief(
        id=f"{date}-utility-{i+1:02d}",
        date=date,
        kind="utility",
        series=fmt["series"],
        title=title,
        hook=hook,
        duration_sec=fmt.get("duration", 24),
        voiceover=voiceover,
        visual_beats=[
            "Start with Exquisite World metaphor",
            "Show screen recording or UI mock of website step",
            "Add Lucía/Kamau/Noura overlay/reaction",
            "Translate action into ritual language",
            "CTA end card",
        ],
        cta=cta,
        production_notes=["Use actual website capture when available", "Do not over-explain", "Make the CTA a world ritual"],
    )


def generate_daily_queue(date: str, count_story: int = 15, count_utility: int = 15) -> list[dict]:
    formats = load_formats()
    story_formats = formats["story_formats"]
    utility_formats = formats["utility_formats"]
    briefs = []
    for i in range(count_story):
        briefs.append(asdict(make_story(i, date, story_formats[i % len(story_formats)])))
    for i in range(count_utility):
        briefs.append(asdict(make_utility(i, date, utility_formats[i % len(utility_formats)])))
    return briefs


def write_queue(date: str, out: str | None = None, count_story: int = 15, count_utility: int = 15) -> Path:
    briefs = generate_daily_queue(date, count_story, count_utility)
    out_path = Path(out) if out else ROOT / "data" / f"daily_queue_{date}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(briefs, indent=2, ensure_ascii=False) + "\n")
    return out_path
