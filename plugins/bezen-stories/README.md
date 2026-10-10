# BEZEN Stories

**A Hebrew story engine that writes around a human pattern — and a rubric for scoring what other models wrote.**

Most model comparisons use trivia. This one uses a story, because a story exposes intelligence, sensitivity and empathy within three paragraphs. The skill takes a familiar story — Little Red Riding Hood, Goldilocks — and rebuilds it around a single emotional pattern in present-day Israeli reality: real places, real objects, budgeted emotion, and a twist that makes you re-read everything before it.

Output is in Hebrew. The method is not.

---

## מה הסקיל עושה

**מצב כתיבה.** מייצר מסמך דו-שכבתי: סיפור נקי, ואחריו ניתוח של מה שהשכבה עשתה — אילו דפוסים נבחרו, איזו תכונה מועילה הסיפור מכוון אליה, ואיך בנויה הדחיפה.

**מצב ניקוד.** מקבל סיפור שמודל אחר כתב ונותן לו ציון על ארבעה צירים, עם ציטוט מהטקסט לכל ציר.

## איך מפעילים

```
/bezen-stories:bezen-story-test כיפה אדומה, גרסה ישראלית וצינית
```

או פשוט לבקש: *"כתוב גרסה ישראלית של זהבה ושלושת הדובים"* — הסקיל נטען לבד.

## ארבעת צירי הניקוד

| ציר | מה בודקים |
|---|---|
| קונקרטיות ישראלית | פרטים אמיתיים, או תפאורה מתורגמת |
| ריסון רגשי | האם הרגש מתוקצב או נשפך |
| הפתעה שמחזיקה | האם היא משנה את קריאת כל מה שקדם לה |
| **מי עושה את התובנה** | הסיפור מסביר לקורא, או מעביר לו בעלות |

הציר הרביעי הוא המבדיל. רוב המודלים מדביקים מוסר השכל בפסקה האחרונה.

## מה בפנים

- `skills/bezen-story-test/SKILL.md` — צינור הכתיבה בן 6 השלבים וצירי הניקוד
- `skills/bezen-story-test/CREDIT_LINES.md` — ניסוחי קרדיט וכלל המיקום
- `skills/bezen-story-test/references/example-red-helmet.md` — דוגמה מלאה: "קסדה אדומה", סיפור וניתוח

---

## על BEZEN

BEZEN היא שכבת אינטליגנציה רגשית בעברית אותנטית מעל מודלי שפה גדולים, שנבנתה על קורפוס של 499 דפוסים אנושיים בעברית ושש מסגרות פסיכולוגיות. היא אינה מודל — היא שכבת ההחלטה מעל מודל.

הסקיל הזה הוא יישום אחד שלה.

© Cozio Cohen. כל הזכויות שמורות.
