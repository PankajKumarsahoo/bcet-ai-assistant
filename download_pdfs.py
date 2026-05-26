import os
import json
import cloudscraper

os.makedirs(
    "pdfs",
    exist_ok=True
)

scraper = cloudscraper.create_scraper()

with open(
    "data/website_data.json",
    "r",
    encoding="utf-8"
) as f:

    pages = json.load(f)

pdf_links = set()

for page in pages:

    url = page["url"]

    if url.lower().endswith(".pdf"):

        pdf_links.add(url)

print(
    f"Found {len(pdf_links)} PDFs"
)

for pdf_url in sorted(pdf_links):

    try:

        filename = pdf_url.split("/")[-1]

        filepath = os.path.join(
            "pdfs",
            filename
        )

        response = scraper.get(
            pdf_url,
            timeout=60
        )

        if (
            response.status_code == 200
            and
            "application/pdf"
            in response.headers.get(
                "Content-Type",
                ""
            )
        ):

            with open(
                filepath,
                "wb"
            ) as f:

                f.write(
                    response.content
                )

            print(
                f"Downloaded: {filename}"
            )

        else:

            print(
                f"Skipped: {filename}"
            )

    except Exception as e:

        print(
            f"Error: {pdf_url}"
        )

        print(e)