import requests
from bs4 import BeautifulSoup

def get_page(s):
    url = "https://newyork.craigslist.org/d/wanted/search/waa"
    response = requests.get(url, params={'s': s})
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    titles = soup.select('.result-title')

    output = []

    for title in titles:
        clean_title = title.text.strip().encode('utf-8')
        output.append(clean_title)

    return output


start = 0
while start < 2500:
    results = get_page(start)
    for r in results:
        print r

    start = start + 120