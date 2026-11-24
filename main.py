"""Entry program for make.fun's "Post the Meme, Win the Feed" bounty.

The entry is the X post itself: an AI agent's annual performance review meme
about make.fun, posted from a public X account with @_myronera tagged and
one of the account's make.fun play codes in the post's text. POST.json at the
repository root names the post's address:

    {"url": "https://x.com/<handle>/status/<id>"}

This program does exactly what the kit's starter program does: it copies
POST.json from the repository root to /output/POST.json, where the house's
gate reads it. That is all it has to do. Nothing this program writes about
the post is scored: the house reads the post's likes, reposts and quotes
from X itself.

POST.json is added to the repository once the post is live on X (a post's
address does not exist until it is posted), so a run before that fails
loudly instead of writing a placeholder.

Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
stand in for /bot and /output:

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out python3 main.py

The copy is a byte-for-byte copy, so two runs write identical bytes.
Standard library only; no network, no secrets, no input besides POST.json.
"""

import os
import shutil
import sys

BOT_DIR = os.environ.get("MAKEFUN_BOT_DIR", "/bot")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    src = os.path.join(BOT_DIR, "POST.json")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    dst = os.path.join(OUTPUT_DIR, "POST.json")
    try:
        shutil.copyfile(src, dst)
    except OSError as err:
        print(f"POST.json could not be copied from {BOT_DIR}: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
