
grocery = {}

while True:
    try:
        item = input()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        print()
        for item, count in sorted(grocery.items()):
            print(f"{count} {item.upper()}")
        break
