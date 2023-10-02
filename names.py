## write file ------------------------------------------------------------

# name = input(f"What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

## read file -------------------------------------------------------------

# with open("names.txt", "r") as file:
#     lines = file.readlines() #assignes names.txt lines to a list called lines

# for line in lines:
#     print("Hello", line.rstrip())

## make it prettier:

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")