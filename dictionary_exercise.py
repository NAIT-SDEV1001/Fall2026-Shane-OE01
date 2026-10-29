# Exercise 1 - Birthday lookup
print("Exercise 1 - Birthdays")

birthdays = {
    "dan": "april 14th",
    "gary": "june 23rd",
    "richard": "february 2nd",
    "jessica": "october 30th",
    "mary": "december 25th",
}

name = input("Enter a name: ").strip().lower()

if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}.")
else:
    print(f"Sorry, we don't have {name}'s birthday.")


# Exercise 2 - Pizza prices
print("\nExercise 2 - Pizza Prices")

# True means the topping is included; False means it is excluded.

BASE_PRICE = 12.0
TIP = 0.18
subtotal = BASE_PRICE

toppings = {
    "cheese": True,
    "pepperoni": True,
    "mushrooms": False,
    "pineapple": False,
    "anchovies": True,
    "olives": False,
    "sausage": True,
}

toppings_prices = {
    "cheese": 0.5,
    "pepperoni": 2.0,
    "mushrooms": 1.0,
    "pineapple": 0.5,
    "anchovies": 1.5,
    "olives": 1.25,
    "sausage": 2.25,
}

print("The toppings of your pizza are:")
for topping, included in toppings.items():
    if included:
        print(topping)
        subtotal +=  toppings_prices[topping]
    else:
        print(f"No {topping}")

tip = subtotal * TIP
total = subtotal + tip

print (f"Your total is: ${total:.2f}")



