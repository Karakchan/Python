# =>  List Comprehension 
# {expression for item in iterable condition}

squres = {x**2 for x in range(5)}
print(squres) #{0, 1, 4, 9, 16}

#0 **2 = 0
#1 **2 = 1
#2 **2 = 4
#3 **2 = 9
#4 **2 = 16

evens = [x for x in range(10) if x%2 == 0]
print(evens) #{0, 2, 4, 6, 8}

uniqchars = [char for char in "Hello Brus"]
print(uniqchars) #['H', 'e', 'l', 'l', 'o', ' ', 'B', 'r', 'u', 's']

numbers = [1,2,3,4,5,6,7,7,2,3]
uninumbers = {x for x in numbers}
print(uninumbers)  #{1, 2, 3, 4, 5, 6, 7}

# => Nested Loopss in list comprehension
 
couplenums = [ (x,y) for x in range(3) for y in range(2)]
print(couplenums) #{(0, 1), (2, 1), (0, 0), (1, 1), (2, 0), (1, 0)}


# => Nested List comprehension  

nestnumberarr = [ [2,3,4],[44,45,65],[400,500,600]]

flatarrs = [y for x in nestnumberarr for y  in x]
print(flatarrs) # [2, 3, 4, 44, 45, 65, 400, 500, 600]

# for x in nestnumberarr  
# first iteration x = [2,3,4]
# second iteration x = [44,45,65]
# third iteration x = [400,500,600]


# for y in x  
# first iteration x = [2,3,4] .process y=2,y=3,y=4
# second iteration x = [44,45,65].process y=45,y=44,y=65
# third iteration x = [400,500,600].process y=400,y=500,y=600
