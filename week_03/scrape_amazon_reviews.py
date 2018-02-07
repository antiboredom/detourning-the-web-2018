import requests
from bs4 import BeautifulSoup
import json
import time

url = 'https://www.amazon.com/Tuscan-Dairy-Whole-Vitamin-Gallon/product-reviews/B00032G1S0/ref=cm_cr_arp_d_paging_btm_31'

def get_page(pagenumber):
    my_params = {
        'ie': 'UTF8',
        'pageNumber': pagenumber,
        'reviewerType': 'all_reviews'
    }

    html = requests.get(url, params=my_params).text
    soup = BeautifulSoup(html, 'html.parser')
    reviews = soup.select('.review')

    output = []

    for review in reviews:
        title = review.select('.review-title')[0].text

        rating = review.select('.review-rating span')[0].text
        rating = rating.replace(' out of 5 stars', '')
        rating = float(rating)

        review_text = review.select('.review-text')[0].text

        item = {
            'title': title,
            'rating': rating,
            'body': review_text
        }

        output.append(item)

    return output


all_reviews = []
for i in range(1, 191):
    try:
        some_reviews = get_page(i)
        all_reviews = all_reviews + some_reviews
        time.sleep(0.5)
    except:
        continue

outfile = open('reviews.json', 'w')
json.dump(all_reviews, outfile, indent=2)
outfile.close()
# print output
# print title, rating, review_text
















