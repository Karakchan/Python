# => Data Containers 

#list 
mylist = [1,2,3,4,5]
print(type(mylist)) #<class 'list'>

#tuple
mytuple = (1,2,3,4,5)
print(type(mytuple)) #<class 'tuple'>

#dict
mydict = {"a":1,"b":2,"c":3}
print(type(mydict)) #<class 'dict'>

#set

myset = {1,2,3,4,5}
print(type(myset)) #<class 'set'>



dict1 = {}
print(type(dict1))   #<class 'dict'>

set1 = {}
print(type(set1))  #<class 'dict'>

#create an empty set
set2 = set()
print(type(set2)) #<class 'set'>

colors = {"red","green","Yellow","white","black"}
print(colors) # {red ...} or {yellow,....} or {white...}

for color in colors:
    print(color)

print("green" in colors) #True


#Adding a single Element
fruits = {"apple","orange"}
print(fruits) #{'apple', 'orange'}

#adding a single element
fruits.add("cherry")
print(fruits) # {'apple', 'cherry', 'orange'}


#adding multi element
fruits.update(["mango","grape"])
print(fruits) #{'apple', 'grape', 'cherry', 'orange', 'mango'}

#remove Elements 
fruits.remove("orange")
print(fruits) #{'apple', 'grape', 'cherry', 'mango'}

#remove element (using discard())
fruits.discard("cherry")
print(fruits) #{'apple', 'grape', 'mango'}

#Clear Element
fruits.clear()
print(fruits) #set()

# => forzonset (Inmutable of set)
fornumbers = frozenset([10,20,30,40,50])
# fornumbers.add(60)  #error
# fornumbers.remove(30) #error
print(fornumbers) #frozenset({40, 10, 50, 20, 30})
print(20 in fornumbers) #True
print(60 in fornumbers) #false

set3 = {1,2,3,6}
set4 = {4,5,6,3}

#Union Combine ( | )
print(set3 | set4) #{1, 2, 3, 4, 5, 6}

#intersetion (&)
print(set3 & set4) #{3, 6}

# Difference ( - )
print(set3 - set4) #{1, 2}
print(set3.difference(set4))  #{1, 2}

print (set4 - set3) #{4, 5}
print(set4.difference(set3)) #{4, 5}

#symmetric Difference (^)
print(set3^set4) #{1, 2, 4, 5}
print(set3.symmetric_difference(set4)) #{1, 2, 4, 5}

