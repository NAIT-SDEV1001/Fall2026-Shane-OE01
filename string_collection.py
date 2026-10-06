#The characters in a string can be iterated through like a list
name = "Shane"

for letter in name:
    print(letter)

#search
search_letter = input("Enter a letter: ")
if search_letter in name:
    print("found it!")

