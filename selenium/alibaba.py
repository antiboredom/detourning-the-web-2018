import sys
import time
from selenium import webdriver

def get_page():
    time.sleep(2)
    items = driver.find_elements_by_css_selector('.m-product-item')
    for item in items:
        title = item.find_element_by_css_selector('.title').text
        try:
            price = item.find_element_by_css_selector('.price').text
        except:
            price = 'UNKNOWN'
        print title, price

    try:
        driver.execute_script("document.querySelector('a.next').click();")
    except:
        driver.quit()
        sys.exit()

    get_page()

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)

url = 'http://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=high+quality+drugs'
driver.get(url)
get_page()
