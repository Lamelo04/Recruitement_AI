import os
import fitz  # PyMuPDF pour PDF
import docx
import pytesseract
from PIL import Image

def extract_text_from_pdf(pdf_path):
    """Extrait le texte d'un fichier PDF."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text

def extract_text_from_docx(docx_path):
    """Extrait le texte d'un fichier DOCX."""
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_image(image_path):
    """Extrait le texte d'une image via OCR."""
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

def extract_text(file_path):
    """Détecte le format et applique l'extraction appropriée."""
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext in [".doc", ".docx"]:
        return extract_text_from_docx(file_path)
    elif ext in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(file_path)
    else:
        raise ValueError("Format non supporté")

# Test du pipeline avec un fichier
if __name__ == "__main__":
    file_path = "CVs/cv-axel.png"  # Remplace avec le chemin de ton fichier
    try:
        extracted_text = extract_text(file_path)
        print("Texte extrait :\n-------------------------------\n", extracted_text)  # Affichage des 500 premiers caractères
    except Exception as e:
        print("Erreur :", e)
