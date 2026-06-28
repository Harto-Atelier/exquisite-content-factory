from __future__ import annotations

import argparse
from .generator import write_queue


def main() -> None:
    parser = argparse.ArgumentParser(prog="exq-content")
    sub = parser.add_subparsers(dest="cmd", required=True)
    gen = sub.add_parser("generate", help="generate daily content queue")
    gen.add_argument("--date", required=True)
    gen.add_argument("--count-story", type=int, default=15)
    gen.add_argument("--count-utility", type=int, default=15)
    gen.add_argument("--out", default=None)
    args = parser.parse_args()
    if args.cmd == "generate":
        path = write_queue(args.date, args.out, args.count_story, args.count_utility)
        print(path)

if __name__ == "__main__":
    main()
