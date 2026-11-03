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
        if value.strip():#if the value after removing spaces  has a value then break
            break
        print("Must enter something!")
    return value
 