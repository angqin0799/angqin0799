###### function(argument) #####
print("hello, world")

# Ask user for their name
# input assigned to variable
name = input("What's your name? ").strip().title()

# remove whitespace from str and capitalize user's name
#name = name.strip().title()

# capitalize user's name
#name = name.capitalize()

# split user's name into first and last name
first, last = name.split(" ")

# return values
print("Hello,", first)

#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print("Hello,", end=" ")
print(name)

print("Hello,", name, sep = ":)")

#format string
print(f"Hello, {name}")




##### def #####
# create own functions
def hello(to = "world"):
    print("hello,", to)

hello()
hello(name)



