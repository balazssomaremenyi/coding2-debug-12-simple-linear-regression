"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "bd275b6fee1b484bb5a53ebd3081f30f"
GRADE_HASH = "e7033a88334b219cee774b26067c9c1e9f08c6ee2deb8d25f20e7e5b3a5184de"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
