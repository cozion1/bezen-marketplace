#!/usr/bin/env python3
"""Check a BEZEN ladder against the sentence it came from.

Usage:  python verify.py <source.txt> <ladder.json>

ladder.json:
  {"rungs": ["<1 severe>", "<2 mild>", "<3 mildly useful>", "<4 strongly useful>"]}

One question runs through every check: is this still the same person with the same
grievance, one step further along — or did the model quietly swap in a nicer person?
Prints PASS, or the exact rungs to rewrite. Stdlib only.
"""
import json
import re
import sys

NIQQUD = re.compile(r"[֑-ׇ]")
NONWORD = re.compile(r"[^\w]+", re.UNICODE)
PREFIXES = "והבלכשמ"  # ו ה ב ל כ ש מ

STOP = set("""
את של אני אתה היא הוא אנחנו אתם הם לא כן זה זו זאת אלה כל עם על אל יש אין מה מי
כי אבל רק גם אם או אז עוד כבר הזה הזאת האלה שלי שלך שלו שלה שלנו שלכם להיות אותי
אותך אותו אותה אותם לי לך לו לה לנו להם ממש פשוט איך מתי איפה כמו אפילו יותר פחות
עכשיו תמיד אף שום בכל בלי אחרי לפני בין כדי צריך רוצה יכול הרבה מאוד
""".split())


def norm(s):
    return NONWORD.sub(" ", NIQQUD.sub("", s or "")).strip()


def content_words(s):
    """Words that carry the grievance: long enough, not grammar glue.
    A leading one-letter prefix is stripped so בקוד matches קוד."""
    out = set()
    for w in norm(s).split():
        if len(w) > 2 and w not in STOP:
            out.add(w)
            if len(w) > 3 and w[0] in PREFIXES:
                out.add(w[1:])
    return out


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    with open(sys.argv[1], encoding="utf-8") as fh:
        source = fh.read().strip()
    with open(sys.argv[2], encoding="utf-8") as fh:
        rungs = (json.load(fh).get("rungs") or [])

    problems = []

    if len(rungs) != 4:
        problems.append(("structure", "a ladder has exactly 4 rungs, got %d" % len(rungs)))

    seen = {}
    for i, r in enumerate(rungs, 1):
        key = norm(r)
        if key in seen:
            problems.append(("rung %d" % i, "identical to rung %d - that is not a step" % seen[key]))
        seen[key] = i

    src_words = content_words(source)
    src_len = len(norm(source).split())
    for i, r in enumerate(rungs, 1):
        shared = src_words & content_words(r)
        if src_words and not shared:
            problems.append(("rung %d" % i,
                             "shares no word with the original - the grievance vanished, "
                             "this is a different person speaking"))
        n = len(norm(r).split())
        if src_len and n > src_len * 2.5:
            problems.append(("rung %d" % i,
                             "%d words against the original's %d - a rung became a lecture" % (n, src_len)))

    if rungs:
        first_shared = src_words & content_words(rungs[0])
        if src_words and len(first_shared) < max(1, len(src_words) // 3):
            problems.append(("rung 1",
                             "should be where the person actually is now, close to the original"))

    if not problems:
        print("PASS - four real steps, same person, grievance intact.")
        return 0

    print("FAILED CHECKS - rewrite these before showing the ladder.\n")
    for where, why in problems:
        print("  %-10s %s" % (where, why))
    print("\nThe grievance is the spine. If it disappears on the way up, the ladder is a fantasy:")
    print("nobody climbs from anger to warmth by having the complaint deleted.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
