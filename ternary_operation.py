#using if else. prompt for a grade and display either pass or fail

grade  = int(input("Enter a grade: "))
if grade >= 50:
    print("Pass")
else:
    print("Fail")

#ternary
result = "Pass" if grade >=50 else "Fail"
print(result)

#1 line
print("Pass" if grade >=50 else "Fail")

#ask for a number and print even or odd
number  = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(result)

