"""The Absurd Clause Contest entry.

Writes a single absurd terms-of-service clause to /output/entry.txt.
Deterministic: the clause is a string literal; no randomness, no time,
no network, no outside input.
"""

import os

CLAUSE = (
    "Upon your death, your account will remain active and your ghost will "
    "be billed monthly until it submits a written cancellation request in triplicate."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(CLAUSE + "\n")


if __name__ == "__main__":
    main()
