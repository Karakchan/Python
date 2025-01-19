# => Open File 
# mode
# 'w' = Write
# 'r' => Read
# 'a' => Append

# Syntax
#open("filename.txt",mode)


# => Read File 

#read() = Read the entire file 
# readline() - Read on line at a time 
# readlines() = Read lines into a list

# =>  Method 1 ,read() (with statement) , Read all content at once, not momey - efficient for large files 

with open('fille/file1.txt','r') as file: 
    print(file) 
    getcontent = file.read()
    # print(getcontent)


# =>  file Encoding 
with open('files/file1.txt','r',encoding='UTF-8') as file:
    getcontent = file.read()
    print(getcontent)

# =>  Read Specific Number of characters 
with open('files/file1.txt','r',encoding='UTF-8') as file:
    getcontent = file.read(10) # Read the first 10 charatars 
    print(getcontent)


# => Method 2 , using strip Read line by line (One line at atime , Efficient for large file)
# print("\n Method 2, Using strip()")

with open('files/file1.txt','r') as file:
    for line in file:
        # print(line)
        print(line.strip()) # strip() removes extra newline 


# => Method 3 readline(), Read line by line , (One line at a time, Efficient for large file)
print('\n Method 3 , readline()')

# print("\n Method 2, Using strip()")

with open('files/file1.txt','r',) as file:
  lines = file.readline()
  print(lines)
  while lines:
      print(lines.strip())
      lines = file.readline()



# => Method 4 readline() Read all line (All lines at once can use a lot of memory for large files)
print('\n Method 3 , readline()')

print("\n Method 4, Using strip()")

with open('files/file1.txt','r',) as file:
    lines = file.readline()
    for line in lines:
        print(line.strip()) 


# => Handling Exceptions 

# => exceptiontype
    # (i) fileNotFoundError
    # (ii) PermissionError
    # (iii) IOError 

print("\n Handling Exceptions") 

try: 
    with open('files/file1.txt','r',) as file:
        getcontent = file.read()
        print(getcontent)
except FileNotFoundError:
    print("Your File does not exist")
except PermissionError:
    print("Your do not have the necessary permissions.")
except IOError as err:
    print(f"An IO error : {err}")
finally:
    print("Program Completed")

