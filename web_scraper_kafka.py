import time
import json
import requests
from bs4 import BeautifulSoup
from kafka import KafkaProducer

# Kafka producer ayarları
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Web scraping fonksiyonu
def scrape_data():
    url = "https://scrapeme.live/shop/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.select('ul.products li')

    data = []
    for product in products:
        product_url = product.select_one('a.woocommerce-LoopProduct-link')['href']
        product_data = scrape_product_detail(product_url)
        if product_data:
            data.append(product_data)
        time.sleep(1)  # Her ürün arasında 1 saniye bekleme ekliyoruz

    return data

def scrape_product_detail(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    name = soup.select_one('h1.product_title').text.strip()

    price_elem = soup.select_one('p.price span.amount')
    if price_elem:
        price = price_elem.text.strip()
    else:
        price = ""

    description_elem = soup.select_one('div.woocommerce-product-details__short-description')
    if description_elem:
        description = description_elem.text.strip()
    else:
        description = ""

    stock_elem = soup.select_one('p.stock')
    if stock_elem:
        stock = stock_elem.text.strip()
    else:
        stock = ""

    product_data = {
        "name": name,
        "price": price,
        "description": description,
        "stock": stock
    }
    return product_data

# Veriyi Kafka'ya gönderme ve dosyaya yazma
def send_data_to_kafka():
    data = scrape_data()
    for item in data:
        producer.send('scraped_data', value=item)
        time.sleep(1)

    # Veriyi dosyaya yazma
    with open('kafka_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    send_data_to_kafka()
