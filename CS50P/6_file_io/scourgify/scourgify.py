import sys, csv

def main():
    # validate user input
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

    iterable = read_input_file(input_file)
    write_output_file(iterable, output_file)

def read_input_file(input_file):
    ''' read before_file & store into iterable '''
    iterable = []

    try:
        with open(input_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                house = row["house"]
                last, first = row["name"].split(",")
                iterable.append({"first": first.lstrip(), "last": last, "house": house})
        return iterable
    except FileNotFoundError:
            sys.exit("Could not read invalid_file.csv")

def write_output_file(iterable, output_file):
    ''' write after file with new headers'''
    with open(output_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for line in iterable:
            writer.writerow(line)

if __name__ == "__main__":
    main()

