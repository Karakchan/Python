# => type of Argument in Python 
# Positional Arguments 
# Keyword Arguments
# Defualt Arguments
# Variable-length Arguments (*args) (Non-Keyword Variable Argument)
# Variable-length Arguments (**kwargs) (Keyword Variable Argument)


# Positional Arguments 
def greet(name,age):
    print(f"Hello friend! my name is {name}, i am {age} years old.")

greet("su su",23)  #Hello friend! my name is su su, i am 23 years old.
greet(25,"Nu Nu")  #Hello friend! my name is 25, i am Nu Nu years old.


# Keyword Arguments 
def hifi(name,age):
    print(f"Hello friend! my name is {name}, i am {age} years old.")

hifi(name="Min Min",age=34) #Hello friend! my name is Min Min, i am 34 years old.
hifi(age=44,name="Su Myat") #Hello friend! my name is Su Myat, i am 44 years old.

# Defualt Arguments

def hime(name,age=18):
    print(f"Hello friend! my name is {name}, i am {age} years old.")

hime("Yamin") # Hello friend! my name is Yamin, i am 18 years old.
hime("Thuzar",20) # Hello friend! my name is Thuzar, i am 20 years old.

# Variable-length Arguments (*args) (Non-Keyword Variable Argument)
def boys(*args):
    print(args)

boys("aung aung") #aung aung
boys("aung aung","kyaw kyaw","zaw zaw") #('aung aung', 'kyaw kyaw', 'zaw zaw')

def solve1(*numbers):
    total = sum(numbers)
    print(f"Sum result is = {total}")

solve1(1,2,3) #6
solve1(34,33,22) #89

def myfunone(num1,*num2):
    print(num1) #1
    print(num2) #2,3,4,5,6

myfunone(1,2,3,4,5,6)


# Variable-length Arguments (**kwargs) (Keyword Variable Argument)

def personinfos(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")

personinfos(name="thuzaw",age=20,city="mawlamyine")
personinfos(name="kaung kayng",professional="Engineers",city="Yangon")

# Exercise (combining Different Type of Arguments)

def emailsender(address,*messages,**files):
    print(f"My Address = {address}")
    if messages:
        for message in messages:
            print(f"Message = {message}")
    if files:
        for key,value in files.items():
            print(f"{key} = {value}")


emailsender("moeook18@gmai.com","Hello admin","I want to request vdo records",lesson="python batch 1",classdate="25/Nov/2024")

def studentinfos(name,age=18,*hobbies,**infos):
    print(f"name = {name}")
    print(f"age = {age}")
    if hobbies:
        for hobbie in hobbies:
            print(f"Hobbies = {hobbie}")
    if infos:
        for key,value in infos.items():
            print(f"{key} = {value}")

studentinfos("nandar")
studentinfos("maugn maung",30)
studentinfos("aung kyaw ",24 , "reading", "travelling")
studentinfos("aung kyaw ",24 , "reading", "travelling",city="bogo",profession="Engineer")



def staffinfos(name,age=18,*hobbies,**infos):
    print(f"name = {name}")
    print(f"age = {age}")
    if hobbies:
        for hobbie in hobbies:
            # print(f"Hobbies = {hobbies}") #Hobbies = ('reading', 'travelling')
            print(f"Hobbies = {','.join(hobbies)}") #Hobbies = reading,travelling
    if infos:
        for key,value in infos.items():
            print(f"{key} = {value}")

staffinfos("aung kyaw ",24 ,"reading","travelling",city="bogo",profession="Engineer")

