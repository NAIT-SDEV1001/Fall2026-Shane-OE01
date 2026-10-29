#print (f"Module Name: {__name__}")
#__name__ will be __main__ if run from the module
#__name__ will be the name of the imported module (snack_shack) if run from where it was imported
#import validation#must prefix the function with name of the module
from .validation import get_valid_integer, get_valid_string
from .pricing import calculate_total#can now just use the function name
from .display import display_item,display_welcome,groovy_welcome,display_receipt

def main():
    groovy_welcome()
    display_welcome()#call the function
    item_input = get_valid_string("Enter Name: ")
    display_item(item_input)#pass an argument into the parameter in the function
    quantity = get_valid_integer("What quantity would you like? ")#call function to get a valid integer for the quantity
    rating = get_valid_integer("enter a rating: ")
    # total = calculate_total(quantity,4.00)#return the total from the function
    total = calculate_total(quantity) #use the default for unit_price
    #total = calculate_total(quantity,10.00)#override the default
    #Pass arguments as keyword arguments
    display_receipt(item_input = item_input, quantity = quantity, total = total)
    groovy_welcome()

#This is a main guard.
#if statement that allows code to only run if it run from the main program(not imported)
if __name__ == "__main__":#if I am running this module directly(not from an import)
    main() 