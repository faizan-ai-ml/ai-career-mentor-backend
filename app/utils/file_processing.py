import os
import shutil
import pdfplumber
import docx
from fastapi import UploadFile, HTTPException

UPLOAD_DIR = "uploads/resumes"

def save_upload_file(upload_file: UploadFile, user_id: int) -> str:
    """
    Saves the uploaded file to uploads/resumes/{user_id}/filename
    Returns the absolute file path.
    """
    try:
        # Create user specific directory
        user_dir = os.path.join(UPLOAD_DIR, str(user_id))
        os.makedirs(user_dir, exist_ok=True)
        
        # Define file path
        file_path = os.path.join(user_dir, upload_file.filename)
        
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
            
        return file_path
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {str(e)}")

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts text from a PDF file using pdfplumber"""
    try:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
        return text
    except Exception as e:
        print(f"Error extracting PDF text: {e}")
        return ""

def extract_text_from_docx(file_path: str) -> str:
    """Extracts text from a DOCX file using python-docx"""
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return "\n".join(full_text)
    except Exception as e:
        print(f"Error extracting DOCX text: {e}")
        return ""

def extract_text_from_file(file_path: str, content_type: str) -> str:
    """Router to choose correct extraction method"""
    if "pdf" in content_type.lower() or file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif "word" in content_type.lower() or "document" in content_type.lower() or file_path.lower().endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        return ""
