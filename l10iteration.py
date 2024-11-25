#  => For in loop
#  Iteration a list
colors = ['red','blue','yellow']

for color in colors:
    print(color)

#  Iteration a string
message = "Hello Karakchan"
print(len(message))

for msg in message:
    print(msg)

# Iteration a dictionary

students = {"name":"su su","city":"Bangkok","age":20}
print(students)
print(students.items())

for key in students:
    print(key,students[key])

for key,value in students.items():
    print(key,"=",value)


# => range() in the loop
for x in range(10):
    print(x)

print(f"Outside x value is {x}")

for y in range(1,5):
    print(y)

print(f"Outside x value is {y}")

for c in range(1,10,5):
    print(c)

print(f"Outside x value is {c}")

# =>break ang contiune (Exit the loop if working and skip the loop if working)

for i in range(1,10):
    if i ==5:
        break # Exit the loop if i = 5
    print(i) # not work cuz break

print(f"Outside i value is {i}")


for q in range(1,10):
    if q == 5:
        continue # skip even number 5
    print(q) #0 1 2 3 4 6 7 8 9

print(f"Outside q value is {q}")


for j in range(10):
    if j % 2 ==0:
        continue
    print(j) # 1 3 5 7 9 

print(f"Outside j value is {i}")


#  Nested loops

staffs = [
    ['aung aung','kyaw kayw','zaw zaw'],
    ['su su','nu nu','yu yu'],
    ['thadar','nilar','muyar']
]

# for staff in staffs:
#     for people in staff:
#         print(people)


# for staff in staffs:
#     for people in staff:
#         print(people)
#     print()


# for staff in staffs:
#     for people in staff:
#         print(people,end=" ")


# for staff in staffs:
#     for people in staff:
#         print(people,end=" ")
#     print()

# => While loop

idx = 0

while idx < 10:
    print(f"Index : {idx}") # 0 to 9
    idx += 1

print(f"Outside idx value is {idx}")  # 10


count = 0

while count < 10:
    count += 1
    print(f"Index : {count}") # 1 to 10

print(f"Outside count value is {count}")  #10

paints = ['red','blue','yellow']
print(paints) #['red', green,'blue']
print(enumerate(paints))  

for index,paint in enumerate(paints):   
    print(index,paint)

index = 0 
while index < len(paints):
    print(index,paints[index])
    index +=1