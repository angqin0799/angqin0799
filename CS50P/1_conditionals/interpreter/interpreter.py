
user_input = input("Expression: ")

x, operator, y = user_input.split(" ")

x = float(x)
y = float(y)

if operator == "+":
    print(x + y)
elif operator == "-":
    print(x - y)
elif operator == "*":
    print(x * y)
else:
    print(x / y)


