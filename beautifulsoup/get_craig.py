import requests
from bs4 import BeautifulSoup

url = "https://newyork.craigslist.org/d/wanted/search/waa"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
# links = soup.select('a')

# for link in links:
#   print link.string
#   print link.get('href')

titles = soup.select('.result-title')
for title in titles:
  print title.text.strip().encode('utf-8')


