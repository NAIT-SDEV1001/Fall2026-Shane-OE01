def get_valid_integer(prompt):
    while True:
        try:
            quantity = int(input(prompt))
            break
        except ValueError:
            print("Please enter a whole number!")
            continue
    return quantity