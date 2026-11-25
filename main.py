"""The Best Meal You Ever Had — entry program.

Writes one sentence about the best meal ever had to /output/entry.txt.
The sentence was chosen by pairwise testing (see candidates.md):
the snapper grilled on a wooden boat off Lombok won 5-0.
"""

import os

SENTENCE = (
    "On a wooden boat off Lombok, a fisherman grilled the snapper "
    "we had just caught, salt and lime and woodsmoke, and I ate it "
    "with my hands while the sun went down."
)


def main() -> None:
    # Gate self-check: the entry must be UTF-8 text of 1-200 characters.
    assert 1 <= len(SENTENCE) <= 200, "sentence outside 1-200 chars"
    assert SENTENCE.strip(), "sentence must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
