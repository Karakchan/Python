# => write File 

# sudo chmod 777 -R files


# mode
# 'w' = Write
# 'r' => Read
# 'a' => Append

# Syntax
#open("filename.txt",mode)


# => Read File 

#write()
#writelines()

#=> Method 1 , write()
print ("\n Mehthod 1 ,write()")

file = open('files/file2.txt', "w")
file.write ("Hello World")
file.close() # always need to close to save changes 

# =>  Method 2 , writelines()
# print("\n Mehthod 2, writelne()")

lines = ["Hello world! \n","This is Python Batch 1 zoom classs. \n", "How to read file in python programming language. \n"]
file = open("files/file3.txt","w")
file.writelines(lines)
file.close()

# =>  Using with statment 
print("\n using with statment")

with open("files/file4.txt","w") as file: 
    file.write("hello world \n")
    file.write("hello sir \n")
    file.write("hello madam \n")


# => Append to a file  
print("\n Append to a file")
with open("files/file5.txt","a") as file:
    file.write("\n This line is append to the file.")

print("\n with variable")

name = "YU YU"
age = 20

with open("files/file6.txt","w") as files:
    file.write(f"My name is {name} and i am {age} year old \n")

# Error handing

print("\n Handling Exceptions") 
try: 
    with open('files/file7.txt','w',) as file:
        file.write("This is python batch 1")
except IOError as err: # General Case 2
    print(f"An IO error : {err}")
finally:
    print("Program Completed")

