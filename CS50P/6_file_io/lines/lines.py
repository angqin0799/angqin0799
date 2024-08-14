import sys

def main():
    file = get_file()
    loc = count_loc(file)
    print(loc)



def get_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file = sys.argv[1]

    if not file.endswith(".py"):
        sys.exit("Not a Python file")
    else:
        return file



def count_loc(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        code_lines = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue
            code_lines += 1

        return code_lines



if __name__ == "__main__":
    main()
