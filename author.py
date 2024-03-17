import requests
from bs4 import BeautifulSoup
import json

def scrape_authors(base_url):
    authors_info = []
    page_number = 1
    while True:
        response = requests.get(f"{base_url}page/{page_number}/")
        soup = BeautifulSoup(response.text, 'html.parser')
        author_elements = soup.find_all(class_='author')
        if not author_elements:
            break
        for author in author_elements:
            name = author.get_text()
            bio_link = author.find_next_sibling('a')['href']
            
            author_response = requests.get(f"{base_url}{bio_link}")
            author_soup = BeautifulSoup(author_response.text, 'html.parser')
            born_date = author_soup.find(class_='author-born-date').get_text()
            born_location = author_soup.find(class_='author-born-location').get_text()
            
            author_info = {
                "fullname": name,
                "born_date": born_date,
                "born_location": born_location,
                "description": "",
                "bio_link": bio_link  
            }
            authors_info.append(author_info)
        page_number += 1
    return authors_info

if __name__ == "__main__":
    base_url = 'http://quotes.toscrape.com/'
    all_authors = scrape_authors(base_url)
    with open('authors.json', 'w') as f:
        json.dump(all_authors, f, indent=2)
