# This script prompts the model defined in model.py with each parsed question and
# record results in a specified folder

import re
from chat import chatbot
import os
import json

exam_folder =  './tex_exam_collection'
answer_folder = './responses'

def extract_questions(file_path):
    with open(file_path,"r", encoding="utf-8") as f:
        text = f.read()
    # Regular expression to capture each question starting with % Question
    pattern = r"(% Question.*?)(?=(% Question|\Z))"
    matches = re.findall(pattern, text, re.DOTALL)
    questions = [match[0].strip() for match in matches]
    return questions

    
for file in os.listdir(exam_folder):
    # Extract question from exam 
    file_path = "tex_exam_collection/Exam 1_Calculus 1.tex"  # os.path.join(exam_folder, file) 
    questions = extract_questions(file_path)
    print(f'Opening {file_path}')
    
    # Pair questions and responses
    qa_pairs = []
    for i, question in enumerate(questions):
        answer = chatbot(question) # Is this the problem?
        qa_pairs.append({
            "question_number": i + 1,
            "question": question,
            "answer": answer
        })

    # Write to JSON
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    out_file = base_name+'_responses.json'
    out_path = os.path.join(answer_folder, out_file)

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(qa_pairs, f, indent=4)
    
    print(f'Saved to {out_path}')
    break