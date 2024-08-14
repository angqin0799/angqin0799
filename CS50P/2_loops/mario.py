
def main():
    print_square(3)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)


def print_square(size):

    # For each row in square
    for i in range(size):
        print("#" * size)
        # # For each brick in row
        # for j in range(size):

        #     # Print brick
        #     print("#", end="")

        # print()

main()
