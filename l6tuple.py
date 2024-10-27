#List Vs Tuple
#1. Mutablity mutable(changeable) and immutable (not changeable)
#2. Perfomance
    #List :Generally slower than tuples
    #list  : Faster and more-efficient . because they are immutable and have a fixed size
#3. Use Case
    # list : need to change , user lists, shopping carts, etc...
    # tuple : geographic coordinates, settings, database records
# 4 . Methods 
    # list :many built-in methods for modifying list. .append(),.remove(),.pop(),.sort()
    #tuple :few built-in methods 

print(type([1,2,3])) # <class 'list'>
print(TypeError((1,2,3))) # <class 'tuple>

# Create a tuple with parenthese
tuple1 = (1,2,3,4,5)

# Create a tuple without parenthese
tuple2 = 11,22,33,44,55


print(tuple1) #(1, 2, 3, 4, 5)
print(tuple2) #(11, 22, 33, 44, 55)

print(tuple1[0])  #1
print(tuple1[3])   #4
print(tuple1[2])    #3

print(tuple2[3])    #44
print(tuple2[4])    #55
print(tuple2[2])    #33


print(tuple1.count(1)) #1
print(tuple1.count(10)) #0

print(tuple2.count(20)) #1
print(tuple2.count(200)) #0


#tuple Upacking
student = 10,20,30,40,50

