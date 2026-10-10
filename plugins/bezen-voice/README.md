# BEZEN Voice

**Your phone bot hears words. It does not hear the caller.**

A caller who says "it's fine, never mind" after a no sounds to a model like a successful ending. It is a customer who gave up. A caller who says "this is the third time I'm calling" gets the original question asked again.

This skill takes the voice agent you already have — Vapi, Retell, ElevenLabs, Twilio, anything with a system prompt — and attaches a layer that changes **how** it speaks, never **what** it does.

Output is in Hebrew.

## מה הסקיל עושה

1. קורא את הפרומפט הקיים שלך ומאתר איפה הוא יאבד מתקשר.
2. מצרף את השכבה בסוף, עם כלל בידוד: אם משהו בשכבה מתנגש עם הוראות העסק — הוראות העסק מנצחות.
3. מראה חמישה מצבים עם תשובת הבוט **לפני** ו**אחרי**: ממהר, מבולבל, תסכול עולה, ויתור שקט, ממעיט בעצמו.
4. אומר מה השכבה לא יכולה לתקן — למשל פרומפט בלי מספר להעברה לאדם.

## הכלל שחוסך את הלקוח

העברה לאדם גם בלי שביקשו, כשהתסכול מופיע פעמיים, כשאותו פרט נכשל פעמיים, או כשהמתקשר מזכיר בריאות, כסף שאבד או מצוקה. שורה אחת:

> "אני מעביר אותך עכשיו לנציג, עם כל מה שכבר אמרת."

## מה הסקיל לא עושה

לא משכתב את הפרומפט שלך — מוסיף בסוף. לא מוסיף הצעות קונקרטיות (מחיר, פיצוי, הנחה). ולא נותן לבוט להכריז על המצב: הוא לעולם לא אומר "אני מבין שאתה לחוץ", הוא פשוט עונה אחרת.

---

© Cozio Cohen. כל הזכויות שמורות.
