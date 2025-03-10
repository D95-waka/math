מתמטיקה
=======

כאן אני שומר את כל המידע שאני יוצר בנוגע למתמטיקה.

מבנה
----

כלל קובצי ה־tex ברפו משתמשים בקובץ [article_base.tex](./article_base.tex) כקובץ הגדרה ראשוני.
קובץ זה משתמש בקובץ [common.lua](./common.lua) לאתחול נוסף של קוד lua.
על כל קובץ tex להיות בתיקייה תחת התיקייה הראשית בלבד, אחרת הם יוגדרו בצורה לא תקינה.

נשים לב כי כלל קובצי ה־tex הם בתקן lualatex, ולא יכולים להתקמפל בסוגים אחרים של latex.
קובץ הבסיס מגדיר כברירת־מחדל שהשפה תהיה עברית, ולכן חשוב לבטל את ההגדרה ידנית בקובץ אם הוא צריך להיות באנגלית.
הפונט בשימוש הוא [Libertinus](https://github.com/alerque/libertinus).

כלל הגדרות סביבת העבודה נמצאות [כאן](https://github.com/D95-waka/DotFiles/tree/master/nvim).

בנייה
-----

תהליך הבנייה צריך להיעשות מהתיקייה בה הקובץ נמצא.

כדי לבנות קובץ כלשהו נוכל להריץ את הפקודה הבאה
```console
lualatex -halt-on-error -output-directory=./bin/ <filename>.tex
```
אפשר להשתמש גם ב־latexmk על־ידי הפקודה הבאה
```console
latexmk -lualatex -interaction=nonstopmode -output-directory=./bin/ <filename>.tex
```

כדי להוסיף כותב ל־pdf יש להריץ את הפקודה הבאה לפני הבנייה:
```bash
export AUTHOR='<author name>'
```
או לחילופין ב־fish:
```fish
set -lx AUTHOR '<author name>'
```
וישנה הפקודה שמאפשרת לנו לקמפל ישירות לצורך הגשה:
```fish
read num && env AUTHOR='<author name>' lualatex -halt-on-error -output-directory=./bin/ "ex$num.tex" && cp -v "bin/ex$num.pdf" ~/Downloads/(basename $PWD)_$num.pdf && git checkout -- bin/ex$num.pdf
```


קורסים
------

רשימת הקורסים שכלולים בתואר.

### קורסים שסיימתי
1. [מתמטיקה דיסקרטית](./discrete_mathematics) – 2022ג'
2. [אלגברה לינארית 1](./linear_algebra_1) – 2023א'
3. [אלגברה לינארית 2](./linear_algebra_2) – 2023ב'
4. [חשבון אינפיניטסימלי 1](./calculus_1) – 2023ב'
5. [חשבון אינפיניטסימלי 2](./calculus_2) – 2024ב'
6. [חשבון אינפיניטסימלי 3](./calculus_3) – 2024ב'
7. [מבנים אלגבריים 1](./algebraic_structures_1) – 2024ב'
8. [תורת הקבוצות](./set_theory) – 2024ב'
9. [תכנות בסיסי בפייתון](https://shnaton.huji.ac.il/index.php/NewSyl/76631) – 2025א'
10. [תורת ההסתברות 1](./probability_theory_1) – 2025א'

### קורסים בלמידה
11. [פונקציות מרוכבות](https://shnaton.huji.ac.il/index.php/NewSyl/80519) – 2025א'
12. [מבוא ללוגיקה](https://shnaton.huji.ac.il/index.php/NewSyl/80423) – 2025א'

### קורסים שילמדו בעתיד
- [אליזה על יריעות](https://shnaton.huji.ac.il/index.php/NewSyl/80416) – 2025ב'
- [אליזה פונקציונלית](https://shnaton.huji.ac.il/index.php/NewSyl/80417) – 2025ב'
- [מבנים אלגבריים 2](https://shnaton.huji.ac.il/index.php/NewSyl/80446/) – 2025ב'
- [מבוא לטופולוגיה](https://shnaton.huji.ac.il/index.php/NewSyl/80516) – 2025ב'
- [לוגיקה מתמטית 2](https://shnaton.huji.ac.il/index.php/NewSyl/80424) – 2025ב'
- [תורת המספרים האלגבריים](https://shnaton.huji.ac.il/index.php/NewSyl/80756) – 2026א'
- [תורת המודלים 1](https://shnaton.huji.ac.il/index.php/NewSyl/80616) – 2026א'
- [תורת המידה](https://shnaton.huji.ac.il/index.php/NewSyl/80517) – 2026א'
- [משוואות דיפרנציאליות](https://shnaton.huji.ac.il/index.php/NewSyl/80320) – 2026ב'
- [כפיה ואי־תלות](https://shnaton.huji.ac.il/index.php/NewSyl/80579) – 2027ב'

יש להוסיף קורס באנגלית וקורס אבני פינה.
