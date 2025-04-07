from models import Models
from pdf_to_tex import pdf_tex
from pathlib import Path
import os

file_path = "./exam_collection" # Exam folder
out_path = "./tex_exam_collection" # Output folder

# convert file and store as .tex files
for file in os.listdir(file_path):
    pdf_tex(f'{file_path}/{file}', out_path)