# Simple Decision Exercise
# Use if/else in the following questions.
# 1.	Prompt the user for two number and display a message indicating if they are equal or not.
 
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))

# if number1 == number2:
#     print("The numbers are equal.")
# else:
#     print("The numbers are NOT equal.")

# #1 print
# result = " "
# if number1 != number2:
#     result = " NOT "

# print(f"The numbers are{result}equal")


# # 2.	Prompt the user for two numbers and display the highest value.
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))

# if number1 > number2:
#     print(f"The highest value is {number1}.")
# elif number2 > number1:
#     print(f"The highest value is {number2}.")
# else:
#     print("They are equal")
     
# # 3.	Prompt the user for two numbers and display the highest value as well as display if it was the second or first number entered. 
# first = int(input("Enter number 1: "))
# second = int(input("Enter number 2: "))

# if first > second:
#     print(f"The highest number between {first} and {second} is {first} and it was the first number entered!")
# elif second > first:
#     print(f"The highest number between {first} and {second} is {second} and it was the second number entered!") 
# else:
#     print ("The numbers are equal")
 
# # 4.	Prompt the user for three numbers and display the highest value. 
# first = int(input("Enter number 1: "))
# second = int(input("Enter number 2: "))
# third = int(input("Enter number 3: "))

# highest = first

# if second > highest:
#     highest = second
# if third > highest:
#     highest = third
# print(f"The highest value is {highest}") 


# # 5.	Prompt the user for a number and display a message indicating if it is even or odd.

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# #1 print 
# result = "Even"
# if number % 2 != 0:
#     result = "Odd"
# print(f"The number is {result}")
 
# 6.	Prompt the user for 2 numbers and a menu to allow them to choose to display the equation and answer for adding, subtracting, multiplying or dividing the numbers. 

number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))
operation = input("Enter an operation to perform (+ - * /): ")

is_valid = True
if operation == "+":
    answer = number1 + number2
    
elif operation == "-":
    answer = number1 - number2
    
elif operation == "*":
    answer = number1 * number2
    
elif operation == "/":
    answer = number1 / number2    
else:
    is_valid = False
    print(f"{operation} is not a valid operation")

#1 print
if is_valid:#same as if is_valid == True
    print(f"{number1} {operation} {number2} = {answer}")

#for checking for false use not
#if not is_valid: #same as if is_valid == False







 
# Challenge: If the user enters an invalid operation, display an error message 
 

