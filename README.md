# מתמטיקה

כאן אני שומר את כל המידע שאני יוצר בנוגע למתמטיקה.

## מבנה
כלל קובצי ה־tex ברפו משתמשים בקובץ<a href="./article_base.tex">article_base.tex</a>כקובץ הגדרה ראשוני.
קובץ זה משתמש בקובץ<a href="./common.lua">common.lua</a>לאתחול נוסף של קוד lua.
על כל קובץ tex להיות בתיקייה תחת התיקייה הראשית בלבד, אחרת הם יוגדרו בצורה לא תקינה.

נשים לב כי כלל קובצי ה־tex הם בתקן lualatex, ולא יכולים להתקמפל בסוגים אחרים של latex.
קובץ הבסיס מגדיר כברירת־מחדל שהשפה תהיה עברית, ולכן חשוב לבטל את ההגדרה ידנית בקובץ אם הוא צריך להיות באנגלית.
הפונט בשימוש הוא [Libertinus](https://github.com/alerque/libertinus).

כלל הגדרות סביבת העבודה נמצאות [כאן](https://github.com/D95-waka/DotFiles/tree/master/nvim).

## בנייה
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


## קורסים
רשימת הקורסים שכלולים בתואר.
<table dir="rtl">
    <tr>
        <th>שם קורס</th>
        <th>זמן</th>
        <th>משקל</th>
    </tr>
    <tr>
        <th colspan="2">הסתיימו</th>
        <th>59</th>
    </tr>
    <tr>
        <td><a href="./discrete_mathematics">מתמטיקה דיסקרטית</a></td>
        <td>2022ג'</td>
        <td>4</td>
    </tr>
    <tr>
        <td><a href="./linear_algebra_1">אלגברה לינארית 1</a></td>
        <td>2023א'</td>
        <td>6</td>
    </tr>
    <tr>
        <td><a href="./linear_algebra_2">אלגברה לינארית 2</a></td>
        <td>2023ב'</td>
        <td>5</td>
    </tr>
    <tr>
        <td><a href="./calculus_1">חשבון אינפיניטסימלי 1</a></td>
        <td>2023ב'</td>
        <td>7</td>
    </tr>
    <tr>
        <td><a href="./calculus_2">חשבון אינפיניטסימלי 2</a></td>
        <td>2024ב'</td>
        <td>7</td>
    </tr>
    <tr>
        <td><a href="./calculus_3">חשבון אינפיניטסימלי 3</a></td>
        <td>2024ב'</td>
        <td>6</td>
    </tr>
    <tr>
        <td><a href="./algebraic_structures_1">מבנים אלגבריים 1</a></td>
        <td>2024ב'</td>
        <td>6</td>
    </tr>
    <tr>
        <td><a href="./set_theory">תורת הקבוצות</a></td>
        <td>2024ב'</td>
        <td>3</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/76631">תכנות בסיסי בפייתון</a></td>
        <td>2025א'</td>
        <td>2</td>
    </tr>
    <tr>
        <td><a href="./probability_theory_1">תורת ההסתברות 1</a></td>
        <td>2025א'</td>
        <td>5</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80519">פונקציות מרוכבות</a></td>
        <td>2025א'</td>
        <td>4</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80423">מבוא ללוגיקה</a></td>
        <td>2025א'</td>
        <td>4</td>
    </tr>
    <tr>
        <th colspan="2">בלמידה</th>
        <th>18</th>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80416">אליזה על יריעות</a></td>
        <td>2025ב'</td>
        <td>4</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80417">אליזה פונקציונלית</a></td>
        <td>2025ב'</td>
        <td>3</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80446/">מבנים אלגבריים 2</a></td>
        <td>2025ב'</td>
        <td>4</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80516">מבוא לטופולוגיה</a></td>
        <td>2025ב'</td>
        <td>4</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80424">לוגיקה מתמטית 2</a></td>
        <td>2025ב'</td>
        <td>3</td>
    </tr>
    <tr>
        <th colspan="2">עתידיים</th>
        <th>19</th>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80616">תורת המודלים 1</a></td>
        <td>2026א'</td>
        <td>2</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80517">תורת המידה</a></td>
        <td>2026א'</td>
        <td>4</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80607">מושגי יסוד בטופולוגיה אלגברית</a></td>
        <td>2026א'</td>
        <td>6</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80756">תורת המספרים האלגבריים</a></td>
        <td>2026ב'</td>
        <td>3</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80320">משוואות דיפרנציאליות</a></td>
        <td>2026ב'</td>
        <td>4</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80421">תורת ההסתברות (2)</a></td>
        <td>2026ב'</td>
        <td>4</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80699">אלגבראות בוליאניות</a></td>
        <td>2026ב'</td>
        <td>2</td>
    </tr>
    <tr>
        <th colspan="3">לא בתוכנית</th>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80650">תורת הקבוצות האקסיומטית</a></td>
        <td>2027א'</td>
        <td>3</td>
    </tr>
    <tr>
        <td><a href="https://shnaton.huji.ac.il/index.php/NewSyl/80579">כפיה ואי־תלות</a></td>
        <td>2027ב'</td>
        <td>2</td>
    </tr>
</table>

יש לעשות שני קורסים באנגלית ולהגיע לסך ניקוד כולל של 124 נקודות זכות.
הסך הכולל הנוכחי הוא 96.
