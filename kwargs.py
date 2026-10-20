# **kwargs accepts any number of keyword arguments 
# Python stores the arguments in a dictionary
# dictionaries store values in key - value pairs 
# {"font":"arial","size":12,"color":"black","margins":"narrow"}

def print_settings(**kwargs):
    #for each key and value in the kwargs dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_settings(font = "arial", size = 12, color = "black",margins = "narrow")

# Question 3 Game settings
# Write display_game_settings(**settings). Print "Game settings:" followed by each key and value in the format key: value. After the settings, print how many were supplied. Use .items() and len(). With no settings, print the heading and "Setting count: 0".
# Sample calls
# display_game_settings(difficulty="easy", sound=True, lives=3)
# display_game_settings()
# Expected output
# Game settings:
# difficulty: easy
# sound: True
# lives: 3
# Setting count: 3
# Game settings:
# Setting count: 0

def display_game_settings(**settings):
    # settings is storing a dictionary containing
    # {"difficult":"easy","sound":True,"lives":3,"resolution":"Hi rez"}
    print("Game Settings:")
    for key, value in settings.items():
        print(f"{key}: {value}")
    print(f"Setting count: {len(settings)}")

display_game_settings(difficult= "easy", sound = True, lives = 3,resolution = "Hi rez")
