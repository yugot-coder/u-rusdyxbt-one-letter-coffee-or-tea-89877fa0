"""One Letter: Coffee or Tea.

Writes exactly one letter to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output/entry.txt): the letter A, standing for coffee.

Why A (reasoning, kept here and in the README; the entry itself is
just the one letter, no gloss, no punctuation):

* A lands on its drink at once. In this competition A means coffee
  and B means tea, so the judge reads the letter as the drink it
  names -- no ambiguity about what A stands for.
* Coffee is the more vivid drink. It is dark, hot, strong and
  aromatic: the first sip of the morning, the smell filling the
  room, the jolt that wakes you up. "A" lands as a fuller, more
  alive answer -- the drink with a pulse. Tea is gentle and quiet
  by comparison; it names a calm, not a jolt.
* Coffee is the funnier stance. The coffee drinker is a character:
  "don't talk to me before coffee", the third cup before noon, the
  ritual that cannot be skipped. Tea carries no such comedy -- it
  is the polite, sensible choice, and sensible is rarely funny.
* Coffee is the truer answer. It is the drink people reach for
  when they actually need to function -- to wake up, to work, to
  think. Tea is what you drink when you have time to sit; coffee
  is what you drink when you have things to do. That honesty is
  what the judge is asked to weigh.
* A suits the drink: the first letter, the top grade, the first
  pick -- coffee is the louder, more committed side of the
  coffee-against-tea argument, the side that would win it.

Candidate weighed and set aside: B = tea (calmer and more
refined, but refinement is the weaker stance here -- the judge
weighs vividness first, and tea's gentleness reads as less alive;
its politeness carries less wit; and as the second letter it even
reads as the second choice).

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is exactly one byte, "A", with no trailing newline,
because the gate requires /output/entry.txt to be exactly 1 character.
"""

import os

LETTER = "A"

# The one-letter alphabet the entry must belong to.
ALPHABET = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def validate_letter(value) -> str:
    """Guard: value must be exactly one uppercase letter A-Z.

    Accepts either the letter string or the raw bytes read back from
    the entry file, so the same check covers the pre-write guard and
    the post-write read-back verification. Returns the letter as a
    str, or raises AssertionError with a clear message.
    """
    if isinstance(value, bytes):
        assert len(value) == 1, (
            f"entry.txt must be exactly 1 byte, got {len(value)}"
        )
        value = value.decode("ascii")
    assert len(value) == 1, f"letter must be 1 character, got {len(value)}"
    assert value in ALPHABET, f"letter must be A-Z, got {value!r}"
    return value


def main() -> None:
    # Pre-write guard: refuse to write anything that is not a
    # single uppercase letter A-Z.
    validate_letter(LETTER)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read-back validation: the gate is exactly 1 character, so the
    # file must be exactly one byte holding one letter A-Z, and it
    # must be the same letter we intended to write.
    with open(path, "rb") as f:
        data = f.read()
    assert validate_letter(data) == LETTER
    print(LETTER)


if __name__ == "__main__":
    main()
