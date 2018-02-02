import requests

url = 'https://duckduckgo.com/ac/'
my_params = {'q': 'The answer is'}

answers = requests.get(url, params=my_params).json()
for answer in answers:
    print answer['phrase']

