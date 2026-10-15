#We want to trap/handle exceptions
#Print a nice error message.
#Keep program running
#Handle exceptions gracefully
#use try/except

# sum = 0
# count = 0
# while True:
#     number =int(input("Enter an integer: "))
#     if number == -1:
#         break
#     sum += number
#     count += 1

# average = sum/count
# print(f"The average is: {average}")    
#What can go wrong?
#Enter a string - ValueError
#Enter a float - ValueError
#Enter -1 as first value - ZeroDivisionError

#use try/except to handle these exceptions
# sum = 0
# count = 0

# while True:
#     try:
#         number = int(input("Enter an integer: "))
#     except ValueError as error_message:
#         print(f"Invalid input. Must be an integer. Error: {error_message}")
#         continue
#     if number == -1:
#         break
#     sum += number
#     count += 1
# try:
#     average = sum/count
#     print(f"The average is: {average}") 
# except ZeroDivisionError:
#     print("No numbers were entered")

#else and finally
# sum = 0
# count = 0

# while True:
#     try:
#         number = int(input("Enter an integer: "))
#     except ValueError as error_message:
#         print(f"Invalid input. Must be an integer. Error: {error_message}")
#         continue
#     else:#executes if there was no exception
#         print("Number accepted")

#     if number == -1:
#         break
#     sum += number
#     count += 1
# try:
#     average = sum/count
#     print(f"The average is: {average}") 
# except ZeroDivisionError:
#     print("No numbers were entered")    
# finally:#Always executes. Even if there is a exit() **DO NOT use exit() in this course
#     #Used for code to clean up(close connections...)/release resources     
#     print("Always executes")
    
# print("Have a groovy day!") 

#multiple exceptions in one try block
# try:
#     number = int(input("Enter an integer: "))
#     result = 100/number
# except ValueError:
#     print("Invalid input. Must be an integer.")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except:
#     print("Unknown error")

#custom exception

# sum = 0
# count = 0

# while True:
#     try:
#         number = int(input("Enter an integer: "))
#         if number < -1:
#             raise ValueError ("Number must be cannot be less than -1")
#     except ValueError as error_message:
#         print(f"Invalid input. Must be an integer. Error: {error_message}")
#         continue
#     if number == -1:
#         break
#     sum += number
#     count += 1
# try:
#     average = sum/count
#     print(f"The average is: {average}") 
# except ZeroDivisionError:
#     print("No numbers were entered")

name = input("Enter your name: ")
try:
    if name == "Sauron":
        raise ValueError ("That name is NO GOOD!")
except ValueError as error_message:
    print(f"Incoming error message! {error_message}")



