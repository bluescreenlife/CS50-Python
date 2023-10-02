def main():
    x = int(input("What is X? "))
    if is_even(x):
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")

# def is_even(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False

def is_even(n):
    return n%2 == 0

main()