import json

infile = open('person.json', 'r')
data = json.load(infile)
# print data
print data['firstName']
print data['favoriteBooks'][0]
infile.close()
