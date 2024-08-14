#test file

def main():
    greeting = input("Greeting: ")
    cashout = value(greeting)
    print(f"${cashout}")


def value(greeting):
    greeting = greeting.strip().lower()
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h") == True:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
