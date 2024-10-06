# => function
# 1.Simple Function with No parameters 
# 2. Function with parameter
#     (i) single parameter
#     (ii) Multi Parameter
# 3.Function with Default Parametar
# 4. Function with a Return Value
# 5. function with multi Return Values
# 6. Lambda Function (Anonymous Function)

# 1.Simple Function with No parameters 

def sayname():
    print('Hello Aung Aung')

sayname()
sayname()

# 2. Function with parameter
    # (i) single parameter

def saycity(city):
    print('Hello ' + city)

saycity("Mandalay")
saycity("Yangon")

def country(country="Thailand"):
    print("Hello " + country)

country("Myanmar")

# 4. Function with a Return Value

def sayage():
    return "I am 25 years old"

print(sayage())


def saynickname(result = "Daw Nge"):
    # result =  "Daw Pu"
    return result

print(saynickname())

def funone(num1,num2):
    result = num1+num2
    return result

print(funone(10,20))



def funtwo(num1,num2=200):
    result = num1+num2
    return f"Total number is = {result}" 

print(funtwo(10))


# 5. function with multi Return Values

def saynameandage():
    name = "honey"
    age = 24
    return name,age

print(saynameandage()) 
    
name,age = saynameandage()
print(name)
print(age)

# 6. Lambda Function (Anonymous Function)

addresult = lambda num1,num2,num3:num1+num2+num3
print(addresult(200,300,400))

sumresult = lambda num1,num2=200,num3=500:num1+num2+num3
print(sumresult(200,300))
print(sumresult(200))

# inputval = input("Enter your name = ")
# msg = "Hello "+ inputval
# msg = "Hello %s" % inputval # don't use
# msg = f"Hello {inputval}" #v3
# print(msg)

firstname = input("Enter your firstname = ")
lastname = input("Enter your lastname = ")
# fullname = "Hello %s%s" % (firstname,lastname) #v2
# fullname = "Hello %s %s" % (firstname,lastname) #v2
fullname = f"Hello {firstname} {lastname} " #v3
print(fullname)