# test file

def main():
    while True:
        fraction_input = input("Fraction: ")
        percentage = convert(fraction_input)
        print(gauge(percentage))
        break

def convert(fraction):
    x, y = map(int, fraction.split("/"))
    if y == 0:
        raise ZeroDivisionError
    elif x <= y:
        return round((x / y) * 100)
    else:
        raise ValueError

def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage:.0f}%"
    elif percentage <= 1:
        return "E"
    else:
        return "F"

if __name__ == "__main__":
    main()
