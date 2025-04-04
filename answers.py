import re
import json # Later used json.dump to store answers?

# This function extracts and returns a list of questions from a .tex file
def extract_questions(path:str):

    with open(path, 'r', encoding='utf-8') as file:
        tex_content = file.read()

    # Split the content by pages
    pages = tex_content.split('\n\n')

    tex_content = '\n\n'.join(pages[1:]) if len(pages) > 1 else tex_content # This is to ignore the first page
    
    # Regex pattern to detect questions
    question_pattern = re.compile(r'\n(\d+\. .*?)(?=\n\d+\. |\Z)', re.DOTALL)
    
    # Store questions
    questions = question_pattern.findall(tex_content)
    return questions



# Test
questions = extract_questions("tex_exam_collection/Exam 1_Calculus 1.tex")

print(f'{questions}')
