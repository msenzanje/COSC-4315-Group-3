import re
import pymupdf as fitz
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

def format_math_to_latex(text):
    # Convert fractions, limits, logarithms, and other mathematical symbols
    text = re.sub(r"lim\s*x→([a-zA-Z0-9±∞-]+)", r"\\lim_{{x \\to \1}}", text)
    text = re.sub(r"log([0-9]+)\s", r"\\log_{\1}", text)
    text = re.sub(r"√\s*([a-zA-Z0-9+*-/]+)", r"\\sqrt{\1}", text)
    text = re.sub(r"ln\s*([a-zA-Z0-9+*-/]+)", r"\\ln{\1}", text)
    
    # Convert exponent notation
    text = re.sub(r"([a-zA-Z0-9]+)\^([a-zA-Z0-9]+)", r"{\1}^{\2}", text)
    
    return text

def pdf_tex(path: str, out_folder: str):
    # Extract .tex text
    extracted_text = extract_text_from_pdf(path)
    latex_text = format_math_to_latex(extracted_text)
    
    # Output file
    base_filename = os.path.splitext(os.path.basename(path))[0]
    output_file = os.path.join(out_folder, f"{base_filename}.tex")

    # Write to file
    print(f'Writing to: {output_file}')
    with open(output_file, "w") as file:
        file.write(latex_text)