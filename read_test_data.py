import PyPDF2

# The following opens an exam and prints the first page
test1C1 =  open("Exam collection/Exam 1_Calculus 1.pdf", "rb")
reader =  PyPDF2.PdfReader(test1C1)

page1 = reader.pages[0]
print(page1.extract_text())