#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from exquisite_content_factory.generator import write_queue

parser = argparse.ArgumentParser()
parser.add_argument("--date", required=True)
parser.add_argument("--count-story", type=int, default=15)
parser.add_argument("--count-utility", type=int, default=15)
parser.add_argument("--out")
args = parser.parse_args()
print(write_queue(args.date, args.out, args.count_story, args.count_utility))
