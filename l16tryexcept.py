# => Exception Handling


#try:
    #exception
# except exceptiontype:
    #code to handle the exception

#=> exception type
    # (i) valueError
    # (ii) ZeroDivisionError


# try:
#     number = int(input("Enter lucky number:"))
#     print(f"Yor lucky number is = {number}")
# except:
#     print("Something went wrong! Please enter a valid number.")

# => Specific Exception 
# try:
#     number = int(input("Enter number :"))
#     print(10/number)
# except ValueError:
#     print("Invalid input ! Please enter a valid number.")
# except ZeroDivisionError:
#     print("You can't divide by zero")

# =>else and finally 

# else Block (optional) = excute only if no exception occurs in the try blocks
# finally Block (Optional) = excute whether or not anexception occurs

# try:
#     number = int(input("Enter number :"))
#     result = 10/number
# except ValueError:
#     print("Invalid input ! Please enter a valid number.")
# except ZeroDivisionError:
#     print("You can't divide by zero")
# else:
#     print(f"Result is = {result}")
# finally:
#     print("Program Completed")

# => Raising Exception  
try: 
    age = int(input("Enter Your age: "))

    if age < 0:
        raise ValueError("Age can't be nagative")
    else:
        print(f"Your age is = {age}")
except ValueError as err:
    print(f"Error is = {err}")