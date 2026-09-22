#if elif
movie = input("Enter a movie: ")
if movie.upper() == "STAR WARS" or movie.upper() == "THE EMPIRE STRIKES BACK" :
    print(f"Use the force! in {movie}")
elif movie.upper() == "JAWS":
    print("Shark!!!")
elif movie.upper() == "INTERSTELLAR":
    print("Space Time")
else:
    print("Unknown movie")

match movie.upper():
    case "STAR WARS" | "THE EMPIRE STRIKES BACK": #| or
        print(f"Use the force! in {movie}")
    case "JAWS":
            print("Shark!")
    case "INTERSTELLAR":
            print("Space Time")
    case _:#anything else
          print("Unknown movie")



    
