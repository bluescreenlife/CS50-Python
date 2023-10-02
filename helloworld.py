## comment
## moar comment

"""
another way to comment
"""

# get user's name
## name = input("What is your name? ")
## say hello to user
## print("Hello,",name)

# another way to print same thing
## print("Hello, " + name)

# override print defaulting to new line
## print("Hello, ", end="")
## print(name)
## print("Hello, \"friend\"")

# printing with f strings / formatted string literals
## print(f"Hello, {name}")
## dog = ["penelope", "cosmo"]
## greetdog = f"Hello, {dog[0]}, who is a good girl? And {dog[1]}. who is a good boy?"
## print(greetdog)

# string methods/functions - strop and titel case a user input
## name = input("What's your name? ").strip().title()
## print(f"Hello, {name}")

#create a hello function

def main(): 
    name = input("What is your name? ").strip().title()
    hello(name)

def hello(name):
    print("Hello, ", name)

main()