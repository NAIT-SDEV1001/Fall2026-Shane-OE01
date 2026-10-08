my_square = int(input("Enter a number to sum the squares: "))
sum = 0

for number in range(1,my_square + 1):
    sum = sum + number ** 2

print(f"The sum of square is: {sum}")

