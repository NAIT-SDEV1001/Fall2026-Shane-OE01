def show_info(name, age):
    print(f"{name} is {age} years old")

class_list = [("Glenn",84),("Alex",22),("Austin",52),("John",47),("Jenn",23),("Bob",64)]

for student in class_list:
    show_info(*student)

