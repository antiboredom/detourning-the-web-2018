import json
from textblob import TextBlob

infile = open('reviews.json', 'r')
reviews = json.load(infile)

all_adjectives = {}

for review in reviews:
    blob = TextBlob(review['body'])
    for tag in blob.tags:
        if tag[1] == 'JJ':
            word = tag[0]
            if word in all_adjectives:
                all_adjectives[word] += 1
            else:
                all_adjectives[word] = 1
            # print tag[0]
    # print review['title']

print all_adjectives
infile.close()
