from models import Models
from pdf_to_tex import pdf_tex
from pathlib import Path
import json
import os

file_path = "./exam_collection" # Exam folder
out_path = "./tex_exam_collection" # Output folder
models =  Models()
llm = models.model_ollama # llama2:latest


# convert file and store as .tex files
for file in os.listdir(file_path):
    pdf_tex(f'{file_path}/{file}', out_path)