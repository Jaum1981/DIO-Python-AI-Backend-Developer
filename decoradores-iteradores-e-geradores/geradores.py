import requests

def fetch_products(url_api, max_pages=100):
    page = 1
    while page <= max_pages:
        response = requests.get(f"{url_api}?page={page}")
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_page' not in data:
            break
        page += 1
   
#uso do gerador     
for product in fetch_products("https://api.example.com/products"):
    print(product)