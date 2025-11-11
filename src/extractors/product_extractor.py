thonimport requests
from bs4 import BeautifulSoup

class ProductExtractor:
    @staticmethod
    def extract_product_details(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        product_details = {
            'product_name': soup.find('h1', {'class': 'product-title'}).text.strip(),
            'product_url': url,
            'price': soup.find('span', {'class': 'price'}).text.strip(),
            'availability': soup.find('span', {'class': 'availability'}).text.strip(),
            'image_url': soup.find('img', {'class': 'product-image'})['src']
        }
        return product_details