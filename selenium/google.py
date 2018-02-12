from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://google.com')

elem = driver.find_element_by_name("q")
elem.send_keys('A spectre is haunting europe')
elem.send_keys(Keys.RETURN)

links = driver.find_elements_by_css_selector('h3.r a')
for link in links:
    print link.get_attribute('href')

driver.quit()
