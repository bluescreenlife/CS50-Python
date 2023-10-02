# x = float(input("What's X? "))
# y = float(input("What's Y? "))

# z = x + y

# print(f"Your rounded total is: {round(z)}")
# print(f"Your rounded total, with comma separator, is: {round(z):,}")
# #                                                            ^ :, adds a comma separator to the string
# print(f"Your total, not rounded, but to two decimals is: {z:.2f}")
# #                                                             ^ specifies number of decimals to print
# print(f"Your total, not rounded, but to three decimals is: {z:.3f}")

def main():
    x = int(input("What is X? "))
    print(f"{x} squared is: ", square(x))

def square(n):
    return pow(n, 2)

if __name__ == "__main__":
    main()