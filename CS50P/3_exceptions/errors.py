''' SyntaxError '''

# What could go wrong?
''' ValueError '''
''' user error - invalid literal for int() with base 10: 'cat' '''

''' NameError '''
''' coder error - sth wrong with ur code '''

''' Error Handling: giving user appropriate error message they can understand '''

##### try #####
''' Best Practice: try the one/minimal line of code that can raise an error '''
##### except ######
##### else ######
##### pass #####



def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))        # error prevent value being assigned to x
        except ValueError:
            pass

            #print("x is not an integer")

        # else:
        #     return x                            # return can break out of loop
'''
try this line of code,
except if sth goes wrong to do this,
else, if nothing goes wrong, do this
'''
main()
