## while loop

# i = 3
# while i != 0:
#     print("meow")
#     i -= 1

## more typical:

# i = 0
# while i < 3:
#     print("meow")
#     i += 1

## for loop

# for i in [0. 1, 2]:
#     print("meow")

# for _ in range(5):
#     print("meow")

## can also do

# print("meow\n" * 3, end="")

## user defined number for loop 

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#        break

# for _ in range(n):
#     print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
        else:
            print("Please entere a positive integer.")

def meow(n):
    for _ in range(n):
        print("meow")

main()