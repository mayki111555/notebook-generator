# notebook-generator

מחולל אוטומטי למחברות לימוד לפיזיולוגיה, ביולוגיה, גנטיקה, ביוכימיה ומיקרוביולוגיה.
הכלי מקבל קבצי טקסט גולמי (כל קובץ מהווה פרק) ומייצר מחברת מרוכזת בסגנון מותאם אישית.

## התקנה
```bash
pip install -e .
```

## שימוש בסיסי
```bash
python -m notebook_generator.cli chapter1.txt chapter2.txt -o notebook.md
```

## ייצוא
ניתן לייצא את המחברת ל‑PDF או Word במידה והכלי `pandoc` מותקן:
```python
from notebook_generator.exporter import Exporter
Exporter('notebook.md').to_pdf('notebook.pdf')
```

## צפייה אינטראקטיבית
```python
from notebook_generator.viewer import NotebookViewer
NotebookViewer('notebook.md').serve()
```
