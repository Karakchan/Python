# => Data Collections (MOdule Containers)

from collections import Counter
getcounts = Counter("Hello World")
print(getcounts) # Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})


# => Queues (from collection module)

from collections import deque

qpersons = deque(['su su','nu nu','Hla Hla'])

qpersons.append('Tun Tun') #add to right end
qpersons.appendleft("SAI SAI") #add to left start

for person in qpersons:
    print(person)

# Remove elements 
qpersons.pop() #Remove from right end
qpersons.popleft() #Remove from left start


for person in qpersons: 
    print(person)

# => Defualtdict (From collections module)

from collections import defaultdict

items = defaultdict(list)

items["fruits"].append("apple")
items["fruits"].append("mango")
items["fruits"].append("banaana")
items["colors"].append("orange")
items["colors"].append("blue")

print(items["fruits"]) #['apple', 'mango', 'banaana']
print(items["colors"]) # ['orange', 'blue']
print(items["candy"]) #[]

numitems = defaultdict(int)

numitems["val"] += 1

print(numitems["val"]) #1