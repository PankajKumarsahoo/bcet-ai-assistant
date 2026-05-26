import os
import json

from pypdf import PdfReader

documents = []

for file in os.listdir("pdfs"):

    if file.endswith(".pdf"):

        path = os.path.join(
            "pdfs",
            file
        )

        try:

            reader = PdfReader(path)

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text

            documents.append(
                {
                    "source": file,
                    "content": text
                }
            )

            print(
                f"Extracted: {file}"
            )

        except Exception as e:

            print(e)

with open(
    "data/pdf_data.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        documents,
        f,
        indent=4,
        ensure_ascii=False
    )

print(
    f"\nSaved {len(documents)} PDFs"
)