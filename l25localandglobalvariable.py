# => Global Variable  

globalval = "I am global"

def myfun1():
    print("Inside Function myfun1 = ", globalval)


# =>  Local Varaible

def myfun2():
    localval = "I am local"
    print("Inside function myfun2 = ",localval)

myfun2() # I am local
# print(localval) #NameError : name "Localval" is not defined 


# => Same Name For local and Global Variable  
globalvar = "I am Global"

def myfun3():
    globalval = "I am Local"
    print("Inside function myfun3 = ",globalval)

myfun3() #I am Local 

print("Outside function myfun3 = ",globalval) # I am Global 


# Exercise 

msg1 = "Hello Sir, This is global variable"

def funone():
    msg2 = "Hi Student, this is local variable"

    print("Inside function funone = ", msg1)
    print("Inside function funone =", msg2)

def funtwo():
    msg1 = "Hello Sir, This is global variable"
    msg2 = "Hi Student, this is local variable"

    print("Inside function funtow =",msg1)
    print("Inside function funtow =",msg2)


def funthree():
    global msg1 # global keyword
    msg1 = "Hello Boss, This is global variable"
    msg2 = "Hi Employee, this is local variable"

    print("Inside function funtow =",msg1)
    print("Inside function funtow =",msg2)


funone()
funtwo()


print("outside function before three, msg1 value", msg1) #sir

funthree() #boss employee

print("outside function after funthree , msg valu1 =", msg1) #boss

# =>  Nested Function and nonlocal keyword

def funfour():
    msg3 = "I am msg3 from outside funfive"

    def funfive():
        nonlocal msg3
        msg3 = " I am msg3 modified by funfive"

    print("Befote invoking funfive" , msg3)
    funfive()
    print("After invoking funfive" , msg3)

funfour()