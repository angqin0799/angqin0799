from tabulate import tabulate
import sys

def main():
    csv_file = get_csv_file()
    table = make_table(csv_file)
    # print(table)
    print(tabulate(table, headers="firstrow", tablefmt="grid"))

def get_csv_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file = sys.argv[1]

    if not file.endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return file

def make_table(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            row = line.strip().split(",")
            lines.append(row)
    return lines

if __name__ == "__main__":
    main()
