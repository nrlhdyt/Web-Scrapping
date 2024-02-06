import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By

baseurl = 'https://www.tokopedia.com/search?st=&q=server%20dell&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource='

driver = webdriver.Chrome()
driver.get(baseurl)

data=[]
for page in range (2):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zeus-root")))
    time.sleep(2)

    for i in range (22):
        driver.execute_script("window.scrollBy(0, 250)")
        time.sleep(1)

    driver.execute_script("window.scrollBy(50, 0)")
    time.sleep(1)


    soup = BeautifulSoup(driver.page_source, "html.parser")
    for items in soup.find_all('div', class_='css-llwpbs'):
        ProductName= items.find('div', class_='prd_link-product-name css-3um8ox').text
        ProductPrice = items.find('div', class_='prd_link-product-price css-h66vau').text
        Address = items.find('span', class_='prd_link-shop-loc css-1kdc32b flip').text
        StoreName = items.find('span', class_='prd_link-shop-name css-1kdc32b flip').text
        try:
            rate = items.find('span', class_='prd_rating-average-text css-t70v7i').text
        except:
            rate = ''
        try:
            soldItems = items.find('span', class_='prd_label-integrity css-1sgek4h').text
        except:
            soldItems = ''
        data.append([StoreName, ProductName, ProductPrice, Address, rate, soldItems])

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']").click()
    time.sleep(3)
    
    
df = pd.DataFrame(data, columns = ['Store', 'Product', 'Price', 'Address', 'Rate', 'Sold Items'])

print(df)
        


#save to excel
df.to_excel(r'C:\Users\hiday\Documents\Python\Tokopedia_Items.xlsx', index=False)
print('Saved')

driver.close()