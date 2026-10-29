#Package-->Modules-->Functions

# from movie_night import display,pricing,validation
# display.display_welcome()

from movie_night.display import display_welcome
from movie_night.pricing import calculate_total
display_welcome()
print(calculate_total(2,3))


