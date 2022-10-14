import os
import smtplib
from bs4 import BeautifulSoup
import requests


AMAZON_LINK = "https://www.amazon.com/All-new-Kindle-Paperwhite-adjustable-Ad-Supported/dp/B08KTZ8249/ref=sr_1_1?crid=4ZS9MXX13CY6&keywords=kindle&qid=1665787266&qu=eyJxc2MiOiI0LjQ4IiwicXNhIjoiNC4xMiIsInFzcCI6IjMuNzkifQ%3D%3D&s=amazon-devices&sprefix=kind%2Camazon-devices%2C216&sr=1-1"

EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('MY_PASSWORD')

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate'
}

response = requests.get(AMAZON_LINK,headers=headers)
webpage = response.text
soup = BeautifulSoup(webpage, 'lxml')

product_title = soup.find('span', id='productTitle').getText().strip()

current_item_price = int(soup.find('span', class_='a-price-whole').getText().replace('.',''))

print(f'The current price of {product_title} is ${current_item_price}.99')

if current_item_price <= 100:
    with smtplib.SMTP('smtp-mail.outlook.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=EMAIL,
            msg=f'Subject:Amazon Price Alert\n\n{product_title}is ${current_item_price}.99\n{AMAZON_LINK}') 