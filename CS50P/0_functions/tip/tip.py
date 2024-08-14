# This program is a tip calculator

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove dollar sign and convert to float
    dollar_float = float(d.replace("$", ""))
    return dollar_float


def percent_to_float(p):
    # Remove parenthesis and convert to a float
    percent_float = float(p.replace("%", "")) / 100
    return percent_float


main()
