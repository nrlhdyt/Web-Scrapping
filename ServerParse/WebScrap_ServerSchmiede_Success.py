import requests
from bs4 import BeautifulSoup
import csv


baseurl = 'https://www.serverschmiede.com/en/server/dell/?page='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

datas = []
for page in range(1,5):
    req = requests.get(baseurl+str(page), headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    items = soup.find_all('li',class_='col_4 gallery_item')

    for x in items:
        name = x.find('div', class_='cath3').text.strip()
        price = ''.join(x.find('div', class_='preisnetto').text.strip().split('\n')) ##untuk menghilangkan enter
        linkImg = x.find('img', class_ ='transition unveil img_border product_image')['src'].replace('/images/product','https://www.serverschmiede.com/images/product') ##untuk mengcopas link, bisa diganti ['href']
        datas.append([name, price, linkImg])



# Menulis CSV File nya
TableHeader = ['Item', 'Price', 'ImageURL']
with open(r'C:\Users\hiday\Documents\Python\ServerSchmiede.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(TableHeader)
    for d in datas:
        writer.writerow(d)
