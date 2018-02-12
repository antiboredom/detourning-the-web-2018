'''
to run:
    python fakenews.py http://foxnews.com 'h1,h2,h3,h4' 'lol'
'''

import sys
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(sys.argv[1])

script = '''
var elements = document.querySelectorAll(arguments[0]);
for (var i = 0; i < elements.length; i++) {
    elements[i].textContent = arguments[1]
}
'''

driver.execute_script(script, sys.argv[2], sys.argv[3])
driver.save_screenshot('screenie.png')
driver.quit()


