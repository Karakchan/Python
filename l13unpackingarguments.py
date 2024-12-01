# => Unpacking Arguments

def sayhi(name,age):
    print(f"Hello friend! My name is {name} and i am {age} years old.")

#  Unpacking positional Arguments 
args = ("Yu Yu",20)

sayhi(*args) #Hello friend! My name is Yu Yu and i am 20 years old.

def addingnumbers(a,b,c):
    print(f"sum result = {a+b+c}")

addingnumbers(1,2,3) #sum result = 6

tuplenumber = (10,20,30)
addingnumbers(*tuplenumber) # sum result = 60

listnumbers = [100,200,300]
addingnumbers(*listnumbers) #sum result = 600

listinfo = {"name":"hla Hla","age":30}
sayhi(**listinfo) #Hello friend! My name is hla Hla and i am 30 years old.