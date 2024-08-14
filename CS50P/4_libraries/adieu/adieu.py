import inflect

p = inflect.engine()

gathered_names = []
adieu_to = ""

while True:
    try:
        input_name = input("Name: ").title().strip()
        gathered_names.append(input_name)
        adieu_to = p.join(gathered_names)
    except EOFError:
        print(f"\nAdieu, adieu, to {adieu_to}")
        break






