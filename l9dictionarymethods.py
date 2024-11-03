
lady = {"name":"Yadanar","age":30}

print(lady) 
print(lady.get('name'))
print(lady.get("gender")) #none
print(lady.get("gender","NOt Described"))

print(lady.keys())
print(list(lady.keys()))
print(list(lady.keys())[0])
print(list(lady.keys())[1])

print(lady.values())
print(list(lady.values()))
print(list(lady.values())[0])
print(list(lady.values())[1])

print(lady.items())
print(list(lady.items()))
print(list(lady.items())[0])
print(list(lady.items())[1])    #('age',30)
print(list(lady.items())[0][1]) #Yandanar
print(list(lady.items())[0][0]) #name
print(list(lady.items())[1][0]) #age
print(list(lady.items())[1][1]) #30

lady.update({"age":30,"gender":"female"})
print(lady) #{'name': 'Yadanar', 'age': 30, 'gender': 'female'}

lady.pop('age')
print(lady)  #{'name': 'Yadanar', 'gender': 'female'}

lady.clear()
print(lady) #{}

girl = {"name":"Yadanar","age":39,"city":"Ye"}

item = girl.popitem() #the last key and value
print(item) #('city', 'Ye')
print(item[0]) #city
print(item[1]) #Ye

print(girl) #{'name': 'Yadanar', 'age': 39}

woman = girl.copy()
print(woman) #{'name': 'Yadanar', 'age': 39}
