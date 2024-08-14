x = int(input("What's x? "))
y = int(input("What's y? "))

z = x + y
print(z)

# comma separation
x = float(input("What's x? "))
y = float(input("What's y? "))

#z = round(x / y, 2)

z = x / y
print(f"{z:,}")

# format how many lagging decimals
print(f"{z:.2f}")

##### def square function #####

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)


main()
