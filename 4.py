#   #4. Return the Item with highest value count
#items = [{'Delhi': 3}, {'Mumbai': 9}, {'Goa': 7}, {'Gujrat': 4}] 
#def highest_count(items):
#Output: Mumbai

def highest_count(items):
    maxCount = 0
    city = ''
    for item in items:
        for key, value in item.items():
            if value > maxCount:
                maxCount = value
                city = key
    return city
items = [{'Delhi': 3}, {'Mumbai': 9}, {'Goa': 7}, {'Gujrat': 4}]
print(highest_count(items)) 
