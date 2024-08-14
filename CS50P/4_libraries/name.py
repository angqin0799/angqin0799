import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments") # sys.argv[0] is the name of the program

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

#print("hello, my name is", sys.argv[1])

