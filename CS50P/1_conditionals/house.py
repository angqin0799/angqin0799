##### match #####
# similar to if, elif, else usage

name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

