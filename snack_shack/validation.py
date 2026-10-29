def get_valid_integer(prompt):
    while True:
        try:
            quantity = int(input(f"{prompt}: "))
            break
        except ValueError:
            print("Please enter a whole number!")
            continue
    return quantity

def get_valid_string(prompt):
    while True:
        value = input(f"{prompt}: ")
        if value.strip():#if the value after removing spaces has a value then break
            break
        print("Must enter something!")       
    return value

# get_valid_string("Enter your name")

# x = "Hello"
# #if x has a value it is True, otherwise it is False
# if x: #if you use this shortcut you can evaluate it for True
#     print("Thank you for saying hello!")
# else:
#     print("Quiet today!")

