import requests
from bs4 import BeautifulSoup
import json

def scrape_quotes(base_url):
    quotes = []
    page_number = 1
    while True:
        response = requests.get(f"{base_url}page/{page_number}/")
        soup = BeautifulSoup(response.text, 'html.parser')
        quote_elements = soup.find_all(class_='quote')
        if not quote_elements:
            break
        for quote in quote_elements:
            text = quote.find(class_='text').get_text()
            author = quote.find(class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all(class_='tag')]
            quote_info = {
                "tags": tags,
                "author": author,
                "quote": text
            }
            quotes.append(quote_info)
        page_number += 1
    return quotes

if __name__ == "__main__":
    base_url = 'http://quotes.toscrape.com/'
    all_quotes = scrape_quotes(base_url)
    with open('quotes.json', 'w') as f:
        json.dump(all_quotes, f, indent=2)
