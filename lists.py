#list is a collection of values
#Each value is stored in an element
#can hold different datatypes (including other lists)

colors = ["red", "blue", "green", "yellow"]
#display the list
print(colors)

#access an element by index (starts at 0)
print(colors[1])

#from end of list
print(colors[-2])

#change the values
colors[2] = "pink"
print(colors)

print(len(colors))

#accessing outside the size is an error
# print(colors[4])

#slices
#get values from a range in the list
letters = ["a","b","c","d","e"]
print(f"First three letters: {letters[0:3]}")
#with slices, the lower boundary is inclusive, upper boundary is exclusive

#omit the starting element
print(f"First three letters: {letters[:3]}")

#omit the ending index if slicing from the end of the list
print(f"Last three letters: {letters[-2:]}")


