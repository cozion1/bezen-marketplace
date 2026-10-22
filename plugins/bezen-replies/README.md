# BEZEN Replies

**Sorting a lead reply into yes / no / question loses the lead.**

The same sentence can be a refusal, a fear, or a request for help. "Sounds interesting, but not now" is not a no — it is someone protecting themselves from a decision. This skill reads what the person is defending, and answers that instead of the words.

Output is in Hebrew, as JSON, so it drops into a CRM or a mail pipeline.

## מה חוזר

```json
{"sort": "כן|לא|שאלה",
 "state": "<המצב מתוך עשרה>",
 "protecting": "<על מה האדם מגן>",
 "dont": "<מה אסור לעשות עכשיו>",
 "action": "<הפעולה הבאה>",
 "send": "auto|human|none",
 "message": "<ההודעה הבאה, 1-3 משפטים>"}
```

`send` הוא השדה שחוסך את התקלות היקרות: כעס, חשד או ספק מועברים לאדם ולא נשלחים אוטומטית. בקשת הסרה מסומנת `none` ולא נשלחת בכלל — גם כדרישת חוק הספאם.

## עשרת המצבים

חשש מהתחייבות · בדיקת מחיר מוקדמת · "שלח לי פרטים" · מחויבות קיימת · ההחלטה אצל אחר · עניין אמיתי · בקשת הסרה · כעס או חשד · לא ברור · בתהליך

לכל מצב יש כלל נפרד למה **לא** לעשות. רוב הנזק בלידים נעשה בפעולה, לא במילים.

## מה הסקיל לא עושה

הוא משנה **איך** עונים, לא **מה** מציעים. מחיר, הנחה, דמו או פגישה נלקחים רק מההנחיות של העסק. בלי הנחיה — לא מציעים שום דבר קונקרטי. זה מה שמאפשר להריץ אותו על כל עסק בלי שימציא הצעות.

---

© Cozio Cohen. כל הזכויות שמורות.
