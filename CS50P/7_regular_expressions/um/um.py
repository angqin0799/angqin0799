import re

def main():
    print(count(input("Text: ")))


def count(s):
    found = re.findall(r'\bum\b', s, re.I)
    return len(found)


if __name__ == "__main__":
    main()
