'''
to run:
    python webtext.py http://foxnews.com 'h1,h2,h3,h4' a sentence goes here
'''

import sys
from selenium import webdriver
from subprocess import call
import time

driver = webdriver.Chrome()
driver.get(sys.argv[1])
time.sleep(5)

words = sys.argv[3:]
for i, word in enumerate(words):
    script = '''
    var elements = document.querySelectorAll(arguments[0]);
    for (var i = 0; i < elements.length; i++) {
      elements[i].textContent = arguments[1]
    }
    '''

    driver.execute_script(script, sys.argv[2], word)
    outname = str(i).zfill(3) + '.png'
    driver.save_screenshot(outname)

driver.quit()

call(['convert', '-delay', '60', '*.png',  '-loop', '0', 'out.gif'])


