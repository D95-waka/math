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
        <th>129</th>
    </tr>
    <tr>
        <td>מתמטיקה דיסקרטית</td>
        <td>2021ג'</td>
        <td>4</td>
    </tr>
    <tr>
        <td>אלגברה לינארית 1</td>
        <td>2022א'</td>
        <td>6</td>
    </tr>
    <tr>
        <td>אלגברה לינארית 2</td>
        <td>2022ב'</td>
        <td>5</td>
    </tr>
    <tr>
        <td>חשבון אינפיניטסימלי 1</td>
        <td>2022ב'</td>
        <td>7</td>
    </tr>
    <tr>
        <td>חשבון אינפיניטסימלי 2</td>
        <td>2023ב'</td>
        <td>7</td>
    </tr>
    <tr>
        <td>חשבון אינפיניטסימלי 3</td>
        <td>2023ב'</td>
        <td>6</td>
    </tr>
    <tr>
        <td>מבנים אלגבריים 1</td>
        <td>2023ב'</td>
        <td>6</td>
    </tr>
    <tr>
        <td>תורת הקבוצות</td>
        <td>2023ב'</td>
        <td>3</td>
    </tr>
    <tr>
        <td>תכנות בסיסי בפייתון</td>
        <td>2024א'</td>
        <td>2</td>
    </tr>
    <tr>
        <td>תורת ההסתברות 1</td>
        <td>2024א'</td>
        <td>5</td>
    </tr>
    <tr>
        <td>פונקציות מרוכבות</td>
        <td>2024א'</td>
        <td>4</td>
    </tr>
    <tr>
        <td>מבוא ללוגיקה</td>
        <td>2024א'</td>
        <td>4</td>
    </tr>
    <tr>
        <td>אנליזה פונקציונלית</td>
        <td>2024ב'</td>
        <td>3</td>
    </tr>
    <tr>
        <td>מבנים אלגבריים 2</td>
        <td>2024ב'</td>
        <td>4</td>
    </tr>
    <tr>
        <td>מבוא לטופולוגיה</td>
        <td>2024ב'</td>
        <td>4</td>
    </tr>
    <tr>
        <td>אליזה על יריעות</td>
        <td>2024ב'</td>
        <td>4</td>
    </tr>
    <tr>
        <td>לוגיקה מתמטית 2</td>
        <td>2024ב'</td>
        <td>3</td>
    </tr>
    <tr>
        <td>תורת המודלים 1</td>
        <td>2025א'</td>
        <td>3</td>
    </tr>
    <tr>
        <td>תורת המידה</td>
        <td>2025א'</td>
        <td>4</td>
    </tr>
    <tr>
        <td>גיאומטריה דיפרנציאלית אלמנטרית</td>
        <td>2025א'</td>
        <td>4</td>
    </tr>
    <tr>
        <td>קוגניציה אנושית למלאכותית</td>
        <td>2025א'</td>
        <td>3</td>
    </tr>
    <tr>
        <td>חישוביות וקוגניציה</td>
        <td>2025א'</td>
        <td>6</td>
    </tr>
    <tr>
        <td>פרספקטיבות חדשות על הוראת מתמטיקה</td>
        <td>2025א'</td>
        <td>2</td>
    </tr>
    <tr>
        <td>תיאוריות בהתפתחות הילד והמתבגר</td>
        <td>2025א'</td>
        <td>2</td>
    </tr>
    <tr>
        <td>הסכסוך הישראלי-פלסטיני א'</td>
        <td>2025א'</td>
        <td>2</td>
    </tr>
    <tr>
        <td>יהודי אתיופיה: עבר, הווה ועתיד</td>
        <td>2025א'</td>
        <td>2</td>
    </tr>
    <tr>
        <td>משוואות דיפרנציאליות</td>
        <td>2025ב'</td>
        <td>4</td>
    </tr>
    <tr>
        <td>תורת ההסתברות (2)</td>
        <td>2025ב'</td>
        <td>3</td>
    </tr>
    <tr>
        <td>תבניות ריבועיות ומספרים P־אדיים</td>
        <td>2025ב'</td>
        <td>2</td>
    </tr>
    <tr>
        <td>טופולוגיה דיפרנציאלית</td>
        <td>2025ב'</td>
        <td>2</td>
    </tr>
    <tr>
        <td>סקס- רביה מינית ממולקולות עד פילים, באנגלית</td>
        <td>2025ב'</td>
        <td>2</td>
    </tr>
    <tr>
        <td>תכנות מתקדם בפייתון</td>
        <td>2025ב'</td>
        <td>2</td>
    </tr>
    <tr>
        <td>הסכסוך הישראלי-פלסטיני ב'</td>
        <td>2025ב'</td>
        <td>2</td>
    </tr>
    <tr>
        <td>קוגניציה וחישוביות של בעלי חיים</td>
        <td>2025ב'</td>
        <td>3</td>
    </tr>
    <tr>
        <td>ממדעים לאמנות</td>
        <td>2025ב'</td>
        <td>2</td>
    </tr>
    <tr>
        <td>מחשבת החינוך</td>
        <td>2025ב'</td>
        <td>2</td>
    </tr>
    <tr>
        <th colspan="2">בלמידה</th>
        <th>8</th>
    </tr>
    <tr>
        <td>יסודות בתורת ההצגות</td>
        <td>2026א'</td>
        <td>3</td>
    </tr>
    <tr>
        <td>יסודות באלגברה קומוטטיבית</td>
        <td>2026א'</td>
        <td>3</td>
    </tr>
    <tr>
        <td>סמינר חבורות לי</td>
        <td>2026א'</td>
        <td>2</td>
    </tr>
    <tr>
        <th colspan="2">עתידיים</th>
        <th>13</th>
    </tr>
    <tr>
        <td>תורת הקבוצות המתקדמת 1</td>
        <td>2026ב'</td>
        <td>3</td>
    </tr>
    <tr>
        <td>יסודות בטופולוגיה אלגברית</td>
        <td>2026ב'</td>
        <td>3</td>
    </tr>
    <tr>
        <td>גאומטריה אלגברית 1</td>
        <td>2026ב'</td>
        <td>3</td>
    </tr>
    <tr>
        <td>סמינר בגאומטריה ודינמיקה</td>
        <td>2026ב'</td>
        <td>2</td>
    </tr>
</table>

בנוסף ישנן הדרישות המספריות:
<table dir="rtl">
    <tr>
        <th>קטגוריה</th>
        <th>דרוש</th>
        <th>בוצע</th>
    </tr>
    <tr>
        <td>קורסים</td>
        <td>24</td>
        <td>0</td>
    </tr>
    <tr>
        <td>סמינרים</td>
        <td>4</td>
        <td>0</td>
    </tr>
</table>
