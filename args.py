# *args are a parameter that accepts a variable number of arguments
# Python collects the arguments into a tuple

def print_numbers(*args):#args is a common name, can be anything
    #loop through the tuple
    for number in args:
        print(number)

print_numbers(1,4,2)
print_numbers(11,14,22,532,365,1231,12,1,23,2)

# Question 1 Snack roll call
# Write display_snacks(*snacks). Print each snack on its own line, starting with a dash. Then print the number of
# snacks. If no snacks are supplied, print only "No snacks packed!". Use a loop and len()

def display_snacks(*snacks):
    if len(snacks) == 0:
        print("no snacks packed!")
    else:
        for snack in snacks:
            print(f"- {snack}") 

    print (f"Snack count: {len(snacks)}")        

display_snacks("cookies","turkey","steak","cake")
    
