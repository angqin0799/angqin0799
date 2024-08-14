import re


def main():
    if ipv4 := validate(input("IPv4 Address: ").strip()):
        print("Valid")
    else:
        print("Invalid")


def validate(ip):
    if re.match(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
