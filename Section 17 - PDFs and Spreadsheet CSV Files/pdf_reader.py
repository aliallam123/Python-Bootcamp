import PyPDF2

# Open PDF in read-binary mode
with open("example.pdf", "rb") as f:
    reader = PyPDF2.PdfFileReader(f)
    text = []

    # Loop through pages and extract text
    for i in range(reader.numPages):
        page = reader.getPage(i)
        text.append(page.extractText())

# Print text from all pages
for page_num, content in enumerate(text, start=1):
    print(f"--- Page {page_num} ---\n{content}\n")
