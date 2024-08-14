import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    pattern = r'''
        ^(?P<hr1>[1-9]|1[0-2])\s?
        (:(?P<min1>[0-5]?[0-9]))?\s?
        \s{1}(?P<period1>AM|PM)
        \s{1}to\s{1}
        (?P<hr2>[1-9]|1[0-2])\s?
        (:(?P<min2>[0-5]?[0-9]))?\s?
        \s{1}(?P<period2>AM|PM)
    $'''

    if matches := re.search(pattern, s, re.X):
        hr1, min1, period1, hr2, min2, period2 = map(matches.group, ["hr1", "min1", "period1", "hr2", "min2", "period2"])

        hr1, hr2 = int(hr1), int(hr2)
        min1 = int(min1) if min1 else 0
        min2 = int(min2) if min2 else 0

        if period1 == "PM" and hr1 != 12:
            hr1 += 12
        elif period1 == "AM" and hr1 == 12:
            hr1 = 0
        if period2 == "PM" and hr2 != 12:
            hr2 += 12
        elif period2 == "AM" and hr2 == 12:
            hr2 = 0 

        return f"{hr1:02}:{min1:02} to {hr2:02}:{min2:02}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
