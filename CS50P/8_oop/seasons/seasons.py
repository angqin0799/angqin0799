from datetime import date
import sys, inflect

p = inflect.engine()

def main():
    dob = validate(input("Date of Birth: "))
    minutes = convert(dob)
    print(f"{number_to_words(minutes)} minutes")

def validate(s):
    try:
        yyyy, mm, dd = map(int, s.split("-"))
    except ValueError:
        sys.exit("Invalid date format. YYYY-MM-DD")
    if mm in range(1, 13) and dd in range(1, 32):
        return s
    else:
        sys.exit("Invalid date range.")

def convert(s):
    dob_date = date.fromisoformat(s)
    daydelta = date.today() - dob_date
    return int(daydelta.total_seconds() / 60)

def number_to_words(n):
    words = p.number_to_words(n, andword="")
    return words.capitalize()

if __name__ == "__main__":
    main()
