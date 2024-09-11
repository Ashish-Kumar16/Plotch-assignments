 #2. count the occurrences of a particular element in the 
#list and output highest occurring element
days = ['sun','mon','mon','tue','wed','thu','fri','sat','mon','thu',]
dic = {}
for day in days:
  if day in dic:
    dic[day] += 1
  else:
    dic[day] = 1
commonElement = max(dic, key=dic.get)
highestOccurence = dic[commonElement]
print(highestOccurence)

