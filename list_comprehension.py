#Given a list [2,4,6,8], use a loop to create a NEW list of each value doubled -> [4,8,12,16]
#Display both lists when done
numbers = [2,4,6,8]
doubled = []

for number in numbers:
    doubled.append(number * 2)

print(numbers)
print(doubled)

#List Comprehension
numbers = [2,4,6,8]

doubled = [number * 2 for number in numbers]

print(numbers)
print(doubled)

#Create a list of 3 names, from that list create a NEW list of all the names in upper case. print new list
names = ["Bob","Sue","Dave"]
upper_names = [name.upper() for name in names] 
print(upper_names)

#if
#new list of only even numbers from another list
numbers = [1,6,8,3,4,9,12,54,42]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)