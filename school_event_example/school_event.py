"""A separate school event program that reuses the snack_shack package."""

# Import three modules from the package.

from snack_shack.display import display_welcome,display_receipt
from snack_shack.pricing import calculate_total
from snack_shack.validation import get_valid_integer,get_valid_string

def main():
    print("School Movie Night - Snack Sales")
    print()
    display_welcome()
    
    item_name = get_valid_string("What snack are we selling?")

    # Reuse the package's input function.
    quantity = get_valid_integer("How many do you want? ")

    # The supplied function checks for integers but accepts zero and negatives.
    # This program adds the school event's rule: quantity must be positive.
    while quantity <= 0:
        print("Please enter a quantity greater than zero.")
        quantity = get_valid_integer("How many do you want? ")

    # Reuse the default price of $4.00 from the pricing module.
    total = calculate_total(quantity)

    print()
    display_receipt(item_name, quantity, total)
    print("Thanks for supporting our school movie night!")


# Run the mainline when this file is executed directly.
if __name__ == "__main__":
    main()
