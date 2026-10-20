print("Question 3 - Game Score Average")
total = 0
count = 0
invalid_count = 0

while True:
    try:
        score = int(input("Enter a score from 0 through 100 (-1 to quit): "))
        if score == -1:
            break
        if score < 0 or score > 100:
            raise ValueError 
            
    except ValueError:
        print("Invalid Score. Must be a number between 0 - 100")
            
    total += score
    count += 1
try:    
    average = total/count
    print(f"Average score: {average}")
except ZeroDivisionError:
    print("No scores were entered, so no average calculation")
#OR
else:
    print(f"Average score: {average}")
