#!/usr/bin/env python3
"""Check a song reading against the writer's own words.

Usage:  python verify.py <lyrics.txt> <draft.json>

The draft is the JSON you produced:
  {"strongest": [{"line": "...", "why": "..."}],
   "fixes": ["כנראה התכוונת ל'...'"],
   "hooks": [{"hook": "...", "chorus": "..."}]}

Everything here answers one question: is this the writer's text, or yours?
Prints PASS or the exact items to drop or replace. Stdlib only.
"""
import json
import re
import sys

NIQQUD = re.compile(r"[֑-ׇ]")
NONWORD = re.compile(r"[^\w]+", re.UNICODE)
QUOTED = re.compile(r"['\"“”‘’](.+?)['\"“”‘’]")
PREFIXES = "והבלכשמ"   # ו ה ב ל כ ש מ
VAV_HEY = "וה"                                   # ו ה


def norm(s):
    """Strip niqqud and punctuation, so a quote matches however it was typed."""
    return NONWORD.sub(" ", NIQQUD.sub("", s or "")).strip()


def edits(a, b):
    """Levenshtein distance between two strings."""
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def check_quotes(draft, source):
    """A strongest line must appear in the lyrics word for word."""
    bad = []
    for item in draft.get("strongest") or []:
        line = norm(item.get("line", "")) if isinstance(item, dict) else ""
        if not line or line not in source:
            bad.append(item.get("line", "") if isinstance(item, dict) else str(item))
    return bad


def check_fixes(draft, source):
    """A fix is a typo fix: 1-2 letters away from something the writer typed.
    Same text changes nothing; further away is a rewrite wearing a fix's clothes."""
    words = source.split()
    bad = []
    for f in draft.get("fixes") or []:
        m = QUOTED.search(f) if isinstance(f, str) else None
        fix = norm(m.group(1)) if m else ""
        if not fix:
            bad.append((f, "no quoted wording found"))
            continue
        n = len(fix.split())
        windows = {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}
        d = min((edits(fix, w) for w in windows), default=99)
        if d == 0:
            bad.append((f, "identical to the text - changes nothing"))
        elif d > 2:
            bad.append((f, "%d edits away - this is a rewrite, not a fix" % d))
    return bad


def check_hooks(draft, lyrics, source):
    """Every hook word must be the writer's (a leading ו/ה is allowed),
    and a hook may not come from the chorus he already repeats."""
    words = set(source.split())
    words |= {w[1:] for w in words if len(w) > 2 and w[0] in PREFIXES}

    def own(w):
        return w in words or (len(w) > 2 and w[0] in VAV_HEY and w[1:] in words)

    counts = {}
    for ln in lyrics.splitlines():
        if norm(ln):
            counts[norm(ln)] = counts.get(norm(ln), 0) + 1
    repeated = [ln for ln, n in counts.items() if n > 1]

    bad = []
    for h in draft.get("hooks") or []:
        hook = norm(h.get("hook", "")) if isinstance(h, dict) else ""
        if not hook:
            bad.append(("(empty)", "no hook text"))
            continue
        foreign = [w for w in hook.split() if not own(w)]
        if foreign:
            bad.append((h["hook"], "words the writer never wrote: " + ", ".join(foreign)))
        elif any(hook in ln for ln in repeated):
            bad.append((h["hook"], "taken from the chorus he already repeats - he has tried it"))
        n = len(hook.split())
        if not foreign and not (2 <= n <= 5):
            bad.append((h["hook"], "%d words - a hook is 2 to 5" % n))
    return bad


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    with open(sys.argv[1], encoding="utf-8") as fh:
        lyrics = fh.read()
    with open(sys.argv[2], encoding="utf-8") as fh:
        draft = json.load(fh)

    source = norm(lyrics)
    quotes = check_quotes(draft, source)
    fixes = check_fixes(draft, source)
    hooks = check_hooks(draft, lyrics, source)
    n_hooks = len(draft.get("hooks") or []) - len(hooks)

    if not (quotes or fixes or hooks) and n_hooks >= 2:
        print("PASS - every quote, fix and hook is the writer's own.")
        return 0

    print("FAILED CHECKS - fix these before showing anything to the writer.\n")
    if quotes:
        print("Strongest lines that are NOT in the lyrics (drop or re-quote exactly):")
        for q in quotes:
            print("  - " + q)
        print()
    if fixes:
        print("Fixes that are not typo fixes (drop them):")
        for f, why in fixes:
            print("  - %s  <-- %s" % (f, why))
        print()
    if hooks:
        print("Hooks that are not usable (replace them):")
        for h, why in hooks:
            print("  - %s  <-- %s" % (h, why))
        print()
    if n_hooks < 2:
        print("Only %d valid hook(s). Find more in the verses and the side lines,\n"
              "where the smallest and most personal detail usually hides.\n" % max(n_hooks, 0))
    return 1


if __name__ == "__main__":
    sys.exit(main())
