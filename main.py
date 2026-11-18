"""Clockmaker's pendulum: a short piece written to relax its reader.

The entry point builds four paragraphs about a pendulum running down in a
clockmaker's workshop, then writes them to ``entry.txt`` under the output
directory. Python 3.13, standard library only, fully deterministic: every
run writes exactly the same bytes.

The text itself is the entry. It shows a scene slowing down rather than
telling anyone to slow down: the pendulum's tick returns again and again,
each time a touch later than the last, until the last tick is barely a
sound at all.
"""

import os


def _paragraphs():
    """Return the four paragraphs of the entry, in reading order."""
    opening = (
        "In the clockmaker's workshop the late light lies across the bench "
        "in one long amber strip. A pendulum ticks, back and forth, back "
        "and forth, in the quiet between the tools."
    )
    slowing = (
        "The tick comes, and then a little later it comes again. Each "
        "swing takes a touch longer than the last, the brass bob rising a "
        "little less high, the sound softer against the wooden case."
    )
    settling = (
        "Dust drifts down through the light and settles on the brass "
        "gears. The room has nothing left to wind, nothing left to hurry, "
        "and the tick keeps its own unhurried time."
    )
    fading = (
        "Then a longer pause. Then another. The last tick is barely a "
        "sound at all."
    )
    return (opening, slowing, settling, fading)


def _assemble(paragraphs):
    """Join paragraphs with a blank line between them."""
    return "\n\n".join(paragraphs)


def main():
    """Write the entry text to ``entry.txt`` in the output directory."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = _assemble(_paragraphs())
    target = os.path.join(output_dir, "entry.txt")
    # Bytes, not text mode: text mode would write the platform's line ends
    # and its default encoding, and the two runs must match byte for byte.
    with open(target, "wb") as handle:
        handle.write(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
