### PRINT BRICKS

# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

#     ## another option

#    # print("#\n" * height, end="")


# main()

### PRINT ?S

# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()

def main(size):
    print_square(size)

def print_square(size):
    for i in range(size): # for each row in square
        print("#" * size, end="")
        print()

main(3)