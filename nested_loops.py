#print out rows and seats for a concert
rows = int(input("Enter number of rows: "))
seats = int(input("Enter number of seats: "))

purchases = []

#for each row we need to print a number of seats
#ask the user for the name of the person in each seat and display that with each seat
for row in range (1,rows + 1):
    for seat in range(1,seats + 1):
        name = input("Enter a name: ")
        purchases.append((row,seat,name))
        print(f"Row {row}, Seat {seat} was purchased by {name}")
print(purchases)

#from the values entered create a list of tuples for each seat [(row,seat,name),(row,seat,name),(row,seat,name),(row,seat,name)]
#print the list
#[(1,1,'Bob'),(1,2,'Sue'),(2,1,'Dave'),(2,2,'Susan')]

#create a report of the list
print("\nSEAT PURCHASE REPORT")
print(f"{'Row':<6}{'Seat':<6}{'Name'}")
print("-" * 30)
for row, seat, name in purchases:
    print(f"{row:<6}{seat:<6}{name}")

print(f"\nTotal seats purchased: {len(purchases)}")




