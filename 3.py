# 3. Merge dictionaries a and b. The resultant dict must contain all items of 
# both dicts. If key is common then the value of key in resultant dict 
# must be the sum of value in a and b.
#a = {'x': 1, 'y': 2, 'z': 3}
#b = {'a': 4, 'b': 5, 'y': 6}
#def dictMerge(a, b):

def dictMerge(a, b):
    merged = a.copy()  
    for key, value in b.items():
        if key in merged:
            merged[key] += value 
        else:
            merged[key] = value  
    return merged
a = {'x': 1, 'y': 2, 'z': 3}
b = {'a': 4, 'b': 5, 'y': 6}
result = dictMerge(a, b)
print(result)
