import requests
from bs4 import BeautifulSoup
import csv

baseurl = 'https://www.modanisa.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

datas= []
for x in range (1,271):
    req = requests.get(f'https://www.modanisa.com/en/dresses-en.list?ck=52enusdwerf&page={x}', headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    products = soup.find_all('div', {'data-testid':'listing-product'})

    for items in products:
        link = items.find('a', {'data-testid':'listing-product-link'})['href'].replace('/en',baseurl +'/en')
        name = items.find('div',{'data-testid':'listing-product-name'}).text.strip()
        try:
            primaryPrice = items.find('div', {'id':'el-product-primary-price'}).text.strip()
        except:
            primaryPrice =''
        try:
            discount = items.find('span', {'data-testid':'listing-secondary-discount'}).text.strip()
        except:
            discount = ''
        price = items.find('div', {'data-testid':'listing-product-price'}).text.strip()

        datas.append([link, name, primaryPrice, discount, price])   


# Print data to console with error handling for encoding
for data in datas:
    try:
        print(data)
    except UnicodeEncodeError:
        print("Error encoding data, skipping...")

# CSV File
TableHeader = ['Link Page', 'Items', 'Price', 'Discount', 'Sale Price']
csv_file_path = r'C:\Users\hiday\Documents\Python\Modanisa_Store.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(TableHeader)
    for data in datas:
        try:
            writer.writerow(data)
        except UnicodeEncodeError:
            print(f"Error encoding data: {data}, skipping...")
