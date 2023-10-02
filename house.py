name = input("what's your name? ")

# if name == "Harry" or "Hermione" or "Ron":
#     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
