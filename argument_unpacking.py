#function that takes 2 arguments (name, age)
def show_info(name,age):
    print(f"{name} is {age} years old")

#test
show_info("Shane",54)

#call the function with a tuple argument containing name,age
person = ("Glenn",84)
show_info(*person)#unpack the tuple into seperate positional arguments
#show_info("Glenn",84)

#person in a dictionary
person_dictionary = {"name":"Donovan","age":24}
show_info(**person_dictionary)#unpack the dictionary into seperate keyword arguments
#show_info(name = "Donovan", age = 24)

