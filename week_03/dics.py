person = {
    "firstName": "Sam",
    "lastName": "Lavigne",
    "age": 1002
}

# print person["age"]
person["age"] = 5
person["hairCount"] = "not much"
# print person

for key in person:
    print key
    print person[key]
