import pytesseract
from pdf2image import convert_from_path

pdf_file = "pdfs/sedg-cell.pdf"

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

images = convert_from_path(
    pdf_file
)

text = ""

for image in images:

    text += pytesseract.image_to_string(
        image,
        lang="eng"
    )

print(text[:5000])