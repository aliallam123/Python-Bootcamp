# 🐍 PDFs & CSVs in Python

### PDFs 📄
- Use `PyPDF2` to read PDFs.
- Open file in `"rb"` (read binary) mode.
- Loop through pages using `reader.getPage(i)` and use `.extractText()`.

### CSVs 📊
- Use Python's built-in `csv` module.
- Use `csv.reader()` to read rows from a file.
- Use `csv.writer()` to create new files or append data.

### Notes
- Always use `with open(...)` to manage files properly.
- `newline=''` helps avoid weird spacing issues in CSVs on Windows.
- PDF text extraction might not always be perfect—depends on how the PDF was created.

---

### 🧠 Quick Tips
- PDF files are binary, so always use `'rb'`.
- For Excel files (.xlsx), use `openpyxl` or `pandas`, but for now we stick with `.csv`.
