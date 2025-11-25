import fitz  # PyMuPDF for PDF reading
import docx  # for DOCX reading
import spacy
import os

# ---------- Load NLP model ----------
nlp = spacy.load("en_core_web_md")

# ---------- Function to extract text from PDF ----------
def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text.strip()

# ---------- Function to extract text from DOCX ----------
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# ---------- Function to load job description ----------
def load_job_description(path="job_description.txt"):
    if not os.path.exists(path):
        print("Warning: job_description.txt not found in your folder!")
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

# ---------- Function to calculate similarity ----------
def calculate_similarity(resume_text, job_desc):
    if not resume_text or not job_desc:
        return 0.0
    resume_doc = nlp(resume_text)
    job_doc = nlp(job_desc)
    return resume_doc.similarity(job_doc)

# ---------- Main Program ----------
if __name__ == "__main__":
    print("---- Resume Similarity Checker ----\n")

    job_desc = load_job_description()
    if not job_desc:
        print("Please create and fill job_description.txt file.")
        exit()

    resume_path = input("Enter your resume file path (PDF or DOCX): ").strip()

    if not os.path.exists(resume_path):
        print("File not found! Please check the path and try again.")
        exit()

    if resume_path.lower().endswith(".pdf"):
        resume_text = extract_text_from_pdf(resume_path)
    elif resume_path.lower().endswith(".docx"):
        resume_text = extract_text_from_docx(resume_path)
    else:
        print("Unsupported file type. Please upload a PDF or DOCX file.")
        exit()

    score = calculate_similarity(resume_text, job_desc)
    print(f"\nSimilarity Score: {round(score * 100, 2)}%")
