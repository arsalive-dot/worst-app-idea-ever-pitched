"""The Worst App Idea Ever Pitched — entry generator.

Writes one sentence pitching the worst, most useless app imaginable
to /output/entry.txt, deterministically.

The pitch: Blinkr solves a problem nobody has (forgetting to blink)
with the deadpan confidence of a real startup — streaks, leaderboards
and a Pro plan for people who blink professionally.
"""

import os

ENTRY = (
    "Blinkr is the app that reminds you to blink — with premium blinking "
    "streaks, blink leaderboards, and a $4.99/month Blink Pro plan for "
    "people who blink professionally."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, path)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
