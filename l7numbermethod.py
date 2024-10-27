num1 = 256.99
print(int(num1)) # 256

num2 = "256"
print(int(num2)) # 256


num3 = "256.00"
#print(int(num3)) # Value Error

num4 = 100
print(abs(num4))  #100

num5 = -100
print(abs(num5)) #100

num6 =  "3.44"
print(float(num6)) #3.44

num7 = 5
print(float(num7)) #5.0

num8 = 4.55663
print(round(num8)) #5
print(round(num8,1)) #4.6
print(round(num8,2)) #4.56
print(round(num8,3)) #4.557

print(pow(2,3)) #8
print(pow(2,5)) #32

print(divmod(10,2)) # (5,0)
print(divmod(100,2)) # (50,0)
print(divmod(30,4)) # (7,2)
print(divmod(100,4)) # (25,0)
print(divmod(10,20)) # (0,20)

print(max(10,20,40,20,30)) # 40
print(min(10,20,40,20,30)) # 10

# print(sum(10,20,40,20,30)) #error
print(sum([10,20,40,20,30])) #120
print(sum((10,20,40,20,30))) #120


# Mathematical Function (from match module)
# To ue the math module ! you need to import

import math

print(math.pow(2,3)) #8.0
print(math.pow(3,3)) #27.0

print(math.sqrt(16)) # 4.0
print(math.sqrt(64)) # 8.0
print(math.sqrt(36)) # 6.0
print(math.sqrt(35)) # 5.916079783099616

print(math.ceil(3.2)) #4
print(math.ceil(3.5)) #4
print(math.ceil(3.0)) #3

print(math.floor(3.2)) #3
print(math.floor(3.7)) #3


# e (Euler number) is approximately
print(math.e) # 2.718281828459045

print(math.log(100,10)) # 2.0 (log base 10 )
print(math.log(81,9)) # 2.0 (log base 10 )

print(math.log(10,2)) #3.3219280948873626
print(math.log(100,2)) #6.643856189774725

# default is e 
print(math.log(100)) #4.605170185988092


print(math.log10(100)) #
print(math.log10(1000)) #3.0 

print(math.log2(8)) #3.0


#math.exp(exponential) , base is e 
print(pow(2.718281828459045,2)) #7.38905609893065
print(math.exp(2)) #7.38905609893065
print(pow(2.718281828459045,3)) #20.085536923187668
print(math.exp(3)) #20.085536923187668

import random

print(random.random()) #0.0664391643560931
print(random.random()) #0.1623880840123999

print(random.randint(1,10)) #return a integer between x , y 

# print(random.uniform(1,2,4)) #

numlists = [10,200,300,400,5000]
print(random.choice(numlists)) #random element from the list

numtuple1 = (10,100,300)
print(random.choice(numtuple1))


numtuple2 = 10,200,400
print(random.choice(numtuple2))