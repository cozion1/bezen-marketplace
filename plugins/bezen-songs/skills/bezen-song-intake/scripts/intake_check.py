#!/usr/bin/env python3
"""Check that the assembled lyrics are made of the person's own words.

Usage:  python intake_check.py <answers.txt> <draft_lyrics.txt>

answers.txt      everything the person actually said, in their own words
draft_lyrics.txt the raw song you assembled from those answers

The whole promise of the intake is: you did not write a single line for them.
This proves it. Any content word in the draft that the person never said is
printed, so you can put their word back. Stdlib only.
"""
import re
import sys

NIQQUD = re.compile(r"[֑-ׇ]")
NONWORD = re.compile(r"[^\w]+", re.UNICODE)
PREFIXES = "והבלכשמ"  # ו ה ב ל כ ש מ

# glue words a line needs to stand up; adding these is arranging, not writing
GLUE = set("""
את של אני אתה את היא הוא אנחנו אתם הם לא כן זה זו זאת אלה כל עם על אל יש אין
מה מי כי אבל רק גם אם או אז עוד כבר הזה הזאת האלה שלי שלך שלו שלה שלנו
אותי אותך אותו אותה אותם לי לך לו לה לנו להם איך מתי איפה כמו אפילו
יותר פחות עכשיו תמיד אף שום בכל בלי אחרי לפני בין כדי אולי ועוד והיה
""".split())


def norm(s):
    return NONWORD.sub(" ", NIQQUD.sub("", s or "")).strip()


def vocabulary(text):
    """Every word the person said, plus each word without a one-letter prefix,
    so בחדר counts as having said חדר."""
    words = set(norm(text).split())
    words |= {w[1:] for w in words if len(w) > 2 and w[0] in PREFIXES}
    return words


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    with open(sys.argv[1], encoding="utf-8") as fh:
        said = vocabulary(fh.read())
    with open(sys.argv[2], encoding="utf-8") as fh:
        draft_raw = fh.read()

    def own(w):
        if w in said or w in GLUE:
            return True
        if len(w) > 2 and w[0] in PREFIXES and w[1:] in said:
            return True
        return False

    foreign = []
    for i, line in enumerate(draft_raw.splitlines(), 1):
        line_n = norm(line)
        if not line_n:
            continue
        for w in line_n.split():
            if len(w) > 2 and not own(w):
                foreign.append((i, w, line.strip()))

    if not foreign:
        print("PASS - every word in the draft is the person's own.")
        return 0

    print("FAILED - words the person never said. Put their word back.\n")
    seen = set()
    for i, w, line in foreign:
        if (i, w) in seen:
            continue
        seen.add((i, w))
        print("  line %-3d %-16s in: %s" % (i, w, line))
    print("\nA word you supplied is a word they will not recognise as theirs,")
    print("and the whole point of this intake is that they do.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
