import sys
from pypdf import PdfReader

if len(sys.argv) < 2:
    print("")
    sys.exit(1)

pdf_path = sys.argv[1]

reader = PdfReader(pdf_path)
text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"

print(text)