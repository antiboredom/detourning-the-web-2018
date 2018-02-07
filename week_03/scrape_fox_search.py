import requests

url = 'http://api.foxnews.com/v1/content/search?q=lol&fields=date,description,title,url,image&section.path=fnc&start=20'


results = requests.get(url).json()
docs = results['response']['docs']
# print docs
for doc in docs:
    print doc['title']


