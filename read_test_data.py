import PyPDF2
from pathlib import Path
from ingest import ingest_file
import ollama

 
# This function returns text content within a PDF file
def extract_text(pdf_path: str) -> str:
    pdf = open(pdf_path, 'rb')
    reader = PyPDF2.PdfReader(pdf)
    n = len(reader.pages)
    extracted = ""
    for page in range(n):
        extracted += reader.pages[page].extract_text()

    return extracted

# Print text in Exam collection folder
pathlist = Path("Exam collection").glob("**/*.pdf")
for path in pathlist:
    ingest_file(file_path = path)
    print(f'{extract_text(str(path))}')