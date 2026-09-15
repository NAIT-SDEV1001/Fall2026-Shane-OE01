print("Intro to Python")
# Comment - do not execute
# to comment 
# multiple lines, highlite the
# lines and ctrl /

# Case sensitive
# Extra spaces do not matter around commands, operators
# Spaces DO matter in indentation (code blocks).
# Strings can use "" OR ''. BE CONSISTENT
print("Hello World")
print('Hello World')
#"" is more common
# print ('Let's have a groovy day!')
print("Let's have a groovy day!")

# Escape characters/sequences - provide a way to perform an action in a string
print("It's a \"groovy\" day")
print('It\'s a "groovy" day')
print("Hello\nWorld") # New line
print("Name:\tShane") # Tab
print("To go to a new line in a string use \\n")

# Variables
# A named box that holds value
# value can change
# names contain only letters, numbers, and _ and cannot start with a number
# use snake_case
# We do not need to declare/create them before use
# cannot be named keywords

# examples of assigning values to variables
first_name = "Shane" # String
age = 54 # integer
price = 12.54 # float
is_valid = True # Boolean

# Using variables with strings
# string contatonation
# + is string contatonation operator in Python
print("Welcome " + first_name)

# To use + with non strings you must cast the variables to strings
print("You are " + str(age) + " years old")

# use a , instead of + and datatype does matter
print("You are",age,"years old")

# preferred way (format strings)
print(f"Hello {first_name}! You are {age} years old")

# Constants - Like a variable but its value must stay the same
# use SCREAMING_SNAKE_CASE
# gives a name to a value
# if the value of the constant changes, everywhere it is used also changes
GST_RATE = 0.04
gst = 100 * GST_RATE

#User Input
#input() always returns a string

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(f"Hello {name}! You are {age} years old.")

#Prompt for 2 number and place them in 2 variables
#Add them together
#Display the sum

#5 + 2 = 7

# number1 = int(input("Enter number 1: "))   
# number2 = int(input("Enter number 2: "))

# sum  = number1 + number2

# print(f"{number1} + {number2} = {sum}")

#Math operators
print(4+6) #10
print(6-4) #2
print(4*6) #24
print(6/3) #2.0 / always returns a float
print(58//5) #floor division (rounds down to whole number)
print (6**23) #Exponent
print (9%4) #modulus 

#Formatting
total = 100.1234567
print(round(total,2)) 
print(round(total,6)) 

print(f"{total:.2f}")
print(f"{total:.6f}")

price = 100
print(f"{price:.2f}")

#Math functions
#import imports the math module which contains math functions and constants
import math

test_value = 5.245435

print(math.ceil(test_value)) #round up to whole number
print(math.floor(test_value)) #round down to whole number
print(math.pow(2,3)) #exponent
print(math.sqrt(9)) #square root
print(math.pi) #pi constant


#prompt the user for 2 numbers and place in 2 variables
#Print the values in each variable
#Swap the values that are in each variable 
#Print the values in each variable

#number1 = 20
#number2 = 30

#number1 = 30
#number2 = 20

number1 = input("Enter number 1: ")
number2 = input("Enter number 2: ")

print("Before")
print (f"Number1: {number1}")
print (f"Number2: {number2}")
#Swap
temp = number1
number1 = number2
number2 = temp

print("After")
print (f"Number1: {number1}")
print (f"Number2: {number2}")










 





