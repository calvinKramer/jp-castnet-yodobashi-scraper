thonimport json

class DataCleaner:
    @staticmethod
    def clean_product_data(data):
        cleaned_data = []
        for product in data:
            cleaned_product = {
                'name': product['productName'],
                'price': product['price'],
                'availability': product['availability'],
                'image_url': product['productImage']
            }
            cleaned_data.append(cleaned_product)
        return cleaned_data