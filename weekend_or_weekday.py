days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days_of_weekend = ("Saturday", "Sunday")

for index, day in enumerate(days_of_week, start = 1):
    print(F"{day} is day number {index} of the week")
    if day in days_of_weekend:
        print(F"{day} is a weekend day")
    else:
        print(F"{day} is a weekday")

