"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: 258 Unicode code points,
UTF-8, not whitespace-only. Python 3.13, standard library only, no network.

The text speaks directly to the judge reading it: it has read a million
sentences, and one more is still waiting just past the last word of this
one -- an unfinished sentence about a small blue door at the end of a
hallway no one walks down anymore. It ends on a question the judge can
only answer by imagining what is behind the door, so the curiosity
outlives the last line.
"""

import os

TEXT = (
    "You have read a million sentences. One of them is still waiting for "
    "you, just past the last word of this one \u2014 a sentence nobody ever "
    "finished writing, about a small blue door at the end of a hallway no "
    "one walks down anymore. What do you think is behind it?"
)


def main() -> None:
    # Gate: 1-280 Unicode code points, not whitespace-only. Verified:
    # this text is exactly 258 code points (260 bytes UTF-8).
    assert 1 <= len(TEXT) <= 280, f"entry length {len(TEXT)} out of range"
    assert TEXT.strip(), "entry must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
