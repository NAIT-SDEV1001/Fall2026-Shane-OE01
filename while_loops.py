#while loops repeat a block of code as long as a condition is True
#useful when you do not know how many times to loop

number = 5
counter = 1
while counter <= number:
    print(counter)
    counter +=1

# ask for numbers, add them up until the user enters "done"
#display the sum

#Use a True loop

print("Enter a number to add. Type done to display the sum")
sum = 0

while True:# an endless loop until break
    number = input("Enter a number: ")
    if number == "done":
        break#break exits the loop
    sum += int(number)
print(sum)

#Boolean flag
keep_going = True
sum = 0
while keep_going:
    number = input("Enter a number: ")
    if number == "done":
        keep_going = False
    else: 
        sum += int(number)
print(sum)    

#loop zero or many times
answer = input("Do you want to loop and play the game? (y,n): ")
while answer == "y":
    print("This the game!")
    print("Isn't it fun?!")
    answer = input("Do you want to loop and play the game again? (y,n): ")

print("Game over! Have a groovy day!")









