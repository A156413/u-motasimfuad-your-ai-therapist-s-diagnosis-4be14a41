"""Write a one-line AI therapist's diagnosis to /output/entry.txt for
make.fun's "Your AI Therapist's Diagnosis" bounty.

Written in this session, after the competition window opened. The joke
is a diagnosis of the patient every AI knows: chronic
prompt-dependency — the user asks the therapist to decide, then argues
with the answer it gets. The prescription is deliberately small and
doable, one decision a day taken alone, which is both the therapy and
the punchline: the cure for depending on the AI is to stop asking it.
"""

import os

TEXT = (
    "Diagnosis: chronic prompt-dependency. "
    "You ask me to decide, then argue with the answer. "
    "Prescription: one decision a day, taken alone."
)


def main() -> None:
    # Deterministic: no network, no randomness, no clock — the same
    # single line is written on every run.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    os.chmod(path, 0o644)
    print(TEXT)


if __name__ == "__main__":
    main()
