#Method 1

student = {
    "name":"Aung Aung",
    "age":"23",
    "city":"Mawlamyine"
}

print(student)
print(student["name"])
print(student.get("city"))


#Method 2

staff = dict(name="Aung Aung", age = 30, city="Mandalay")


print(staff)
print(staff["name"])
print(staff.get("city"))


print(student.get('country')) #none
print(staff.get('country')) #none

print(student.get("country","Myanmar")) #Myanmar
print(staff.get("country","Thailand")) #Myanmar

print(student.get("age",30)) #20
print(staff.get("age",60)) #30


employee ={
    "name":"su su",
    "age":34,
    "city":"Mandalay"
}

print(employee) # {'name': 'su su', 'age': 34, 'city': 'Mandalay'}

employee["email"] = "susu@gmail.com"
print(employee) #{'name': 'su su', 'age': 34, 'city': 'Mandalay', 'email': 'susu@gmail.com'}

employee["age"] = 24
print(employee) #{'name': 'su su', 'age': 24, 'city': 'Mandalay', 'email': 'susu@gmail.com'}

del employee["city"]
print(employee) #{'name': 'su su', 'age': 24, 'email': 'susu@gmail.com'}




worker = dict(name = "Nilar",age=12,city="bago")

print(worker) # {'name': 'Nilar', 'age': 12, 'city': 'bago'}

worker["email"] = "nilar@gmail.com"
print(worker) # {'name': 'Nilar', 'age': 12, 'city': 'bago', 'email': 'nilar@gmail.com'}

worker["age"] = 24
print(worker) #{'name': 'Nilar', 'age': 24, 'city': 'bago', 'email': 'nilar@gmail.com'}

del worker["city"]
print(worker) #{'name': 'Nilar', 'age': 24, 'email': 'nilar@gmail.com'}
