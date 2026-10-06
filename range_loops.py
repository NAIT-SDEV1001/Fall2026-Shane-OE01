#range() - generates a sequence of numbers(think of it as a list of numbers)
#can be used as for a loop counter

#syntax 
#range(start,stop,step)
#start is inclusive, stop is exclusive

#print numbers 1 to 5
for number in range(1,6):#loops 5 times
    print(number)

#print the cubes of numbers from 0 to 4 inclusive
for number in range(0,5):
    print(number ** 3)

#print the even numbers between 6 and 80
for number in range(6,81,2):   
    print(number)

#print a countdown from 10 --> 0
for number in range(10,-1,-1):
    print(number)

#ask the user for how many times to print ("Happy Monday!")
number_of_times = int(input("How many times: "))
for count in range(number_of_times):#like slices you can omit the start value
    print("Happy Monday!")

