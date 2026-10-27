#Dictionaries store key-value pairs
#Keys are unique. Strings or numbers
#Values can any datatype,including other dictionaries, lists, tuples

#example
student = {"name":"Archibald","age":42,"email":"Archibald123@gmail.com"}

#access by key
print(student["name"])#retrive a value
student["age"] = 52#update a value
student["city"] = "Bridgetown"

#user creates a new key
key = input("Enter a new key: ")
value = input("Enter a new value: ")
student[key] = value

print(student)

#remove a key and value
del student["age"]

#what happens here? KeyError
# print(student["shoe_size"])
# del student["shoe_size"]

#check if key is in the dictionary
if "cityyyyyyyy" in student:
    del student["cityyyyyyyy"]

#retrieve value with no error if not exist
#get will return None if the key does not exist
print(student.get("city"))
#get can return a default if the key does not exist
print(student.get("student_number","No Student Number"))

#Nested dictionary
inventory = {
            "apples":{"price":.50,"stock_count":40},
            "bananas":{"price":.30,"stock_count":140},
            "watermelon":{"price":5.00,"stock_count":20}
}

print(inventory["apples"]["price"])
print(inventory["apples"]["stock_count"])

#Loop through a dictionary
grades = {"Homer":40, "Bart":12, "Lisa": 98}
#keys
for key in grades:#.keys():#keys() is the default and can be ommited
    print(f"{key}: {grades[key]}")

#Loop through values
total = 0
for grade in grades.values():
    total += grade

print(f"Average grade: {total/len(grades)}")

#Both keys and values
for name,grade in grades.items():
    print(f"{name}: {grade}")

#sort by key
for name,grade in sorted(grades.items()):
    print(f"{name}: {grade}")
#reverse
for name,grade in sorted(grades.items(), reverse = True):
    print(f"{name}: {grade}")

inventory = {"apples":0,"bananas":0, "mangos":0}
purchases = ["apples", "bananas","apples", "mangos","apples"]

#process the purchases to adjust the inventory count
#apples: 3
#bananas: 1
#mangos: 1

#process purchases
for item in purchases:
    inventory[item] += 1
#print inventory
for item,count in inventory.items():
    print(f"{item}: {count}")





