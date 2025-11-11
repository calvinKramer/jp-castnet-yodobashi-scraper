import requests
from bs4 import BeautifulSoup
import json
import time
import os

class YodobashiScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

    def fetch_product_page(self, product_url):
        response = requests.get(product_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def extract_product_data(self, product_url):
        soup = self.fetch_product_page(product_url)
        product_data = {
            'productName': soup.find('h1', {'class': 'product-title'}).text.strip(),
            'productUrl': product_url,
            'price': soup.find('span', {'class': 'price'}).text.strip(),
            'availability': soup.find('span', {'class': 'availability'}).text.strip(),
            'productImage': soup.find('img', {'class': 'product-image'})['src'],
            'productSpecs': soup.find('div', {'class': 'product-specifications'}).text.strip()
        }
        return product_data

    def scrape(self, product_urls):
        products = []
        for url in product_urls:
            try:
                product = self.extract_product_data(url)
                products.append(product)
                time.sleep(1)  # Rate limit
            except Exception as e:
                print(f"Error scraping {url}: {e}")
        return products

def save_data_to_file(data, filename='data/sample_output.json'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    scraper = YodobashiScraper('https://www.yodobashi.com')
    product_urls = ['https://www.yodobashi.com/product/100000001004176517/']  # Example URL
    scraped_data = scraper.scrape(product_urls)
    save_data_to_file(scraped_data)