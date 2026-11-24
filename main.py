"""One line, under 200 characters, of the funniest excuse to call in sick: half believable, fresh, laugh before the last word.

The program writes exactly those lines and nothing else to /output/entry.txt.
"""

import os

TEXT = "I can't come in today — my wisdom tooth declared independence overnight, my face has joined its side, and I am currently in peace talks with an ice pack."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
