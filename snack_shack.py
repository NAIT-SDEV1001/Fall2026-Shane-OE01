#A function is a block of code that performs a task.You define it once and call it many times by name

#Why use functions?
#code reuse
#break code down into smaller problems
#test and debug functions seperately

def display_welcome():
    print("Welcome to the Snack Shack!")
    print("Most snacks are $4.00 each.")

def display_item(item_name):
    print(f"Preparing {item_name}")

def calculate_total(quantity_wanted, unit_price = 4.00):
    total = quantity_wanted * unit_price
    return total

def display_receipt(item_input, quantity, total):
    print(f"Snack: {item_input}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total:.2f}")

def groovy_welcome():
    print("Hope your having a groovy day")   

#function to get a valid integer
def get_valid_integer(prompt):
    while True:
        try:
            quantity = int(input(prompt))
            break
        except ValueError:
            print("Please enter a whole number!")
            continue
    return quantity

groovy_welcome()
display_welcome()#call the function
item_input = input("Snack name: ")
display_item(item_input)#pass an argument into the parameter in the function
quantity = get_valid_integer("What quantity would you like? ")#call function to get a valid integer for the quantity
rating = get_valid_integer("enter a rating: ")
# total = calculate_total(quantity,4.00)#return the total from the function
total = calculate_total(quantity) #use the default for unit_price
#total = calculate_total(quantity,10.00)#override the default
#Pass arguments as keyword arguments
display_receipt(item_input = item_input, quantity = quantity, total = total)
groovy_welcome()