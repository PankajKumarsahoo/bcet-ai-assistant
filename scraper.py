from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import time

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

BASE_URL = "https://bcetodisha.ac.in/"

driver.get(BASE_URL)

time.sleep(10)

html = driver.page_source

soup = BeautifulSoup(
    html,
    "html.parser"
)

links = set()

for a in soup.find_all("a", href=True):

    href = urljoin(
        BASE_URL,
        a["href"]
    )

    if "bcetodisha.ac.in" in href:

        links.add(href)

print(f"Found {len(links)} links")

pages = []

for link in sorted(links):

    try:

        driver.get(link)

        time.sleep(3)

        soup = BeautifulSoup(
            driver.page_source,
            "html.parser"
        )

        title = ""

        if soup.title:
            title = soup.title.text.strip()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        pages.append(
            {
                "url": link,
                "title": title,
                "content": text
            }
        )

        print("Scraped:", link)

    except Exception as e:

        print("Error:", link)

driver.quit()

with open(
    "data/website_data.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        pages,
        f,
        ensure_ascii=False,
        indent=4
    )

print(
    f"Saved {len(pages)} pages"
)