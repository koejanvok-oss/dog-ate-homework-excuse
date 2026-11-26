"""Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one line to /output/entry.txt: the excuse a dog gives after
being caught eating the homework, in the dog's own voice.
"""

LINE = (
    "You left it on the table at nose height \u2014 "
    "that is not homework, that is a buffet with instructions on it."
)


def main() -> None:
    import os

    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
