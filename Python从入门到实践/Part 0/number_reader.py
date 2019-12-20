import json

filename = 'numbers.json'
with open(filename) as j_obj:
    numbers = json.load(j_obj)

print(numbers)
