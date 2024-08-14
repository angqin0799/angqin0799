'''VERSION 2'''
def main():
    while True:
        fraction_input = input("Fraction: ")
        percentage = convert(fraction_input)
        if percentage != None:
            print(gauge(percentage))
            break

def convert(fraction):
    try:
        x, y = map(int, fraction.split("/"))
        if x <= y:
            return round((x / y) * 100)
        else:
            return None
    except (ValueError, ZeroDivisionError):
        return None


def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage:.0f}%"
    elif percentage <= 1:
        return "E"
    else:
        return "F"

if __name__ == "__main__":
    main()

''' VERSION 1'''
# def main():
#         gauge = verify_input("Fraction: ")
#         print(gauge)


# def verify_input(prompt):
#     while True:
#         input_str = input(prompt)
#         try:
#             x , y = map(int, input_str.split("/"))
#             if x <= y:
#                 percentage = x / y * 100
#                 if 1 < percentage < 99:
#                     gauge_output = "{:.0f}%".format(percentage)
#                     return gauge_output
#                 elif percentage <= 1:
#                     return ("E")
#                 else:
#                     return ("F")
#             else:
#                 pass
#         except (ValueError, ZeroDivisionError):
#             pass


# main()
