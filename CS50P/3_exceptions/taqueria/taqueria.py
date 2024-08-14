
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_price = 0
while True:
    try:
        menu_item = input("Item: ").title().strip()
        if menu_item in menu:
            item_price = menu[menu_item]
            total_price += item_price
            print(f"Total: ${total_price:.2f}")
        else:
            pass
    except KeyError:
        pass
    except EOFError:
        print()
        break





