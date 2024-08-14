
##### while #####
'''
counter = 3
while counter boolean expression:
    argument
    counter -= 1
'''

##### for #####
'''
for variable in range(n):
    argument
'''


def main():
    print("eow\n" * 3, end = "")

    for _ in range(3):      # _ represent a variable that will not be used later (pythonic convention)
        print("mew")


    number = get_number()
    meow(number)




def get_number():
    ''' verify user input, induce an infinite loop
    & only break out of loop only if provided positive int input '''
    while True:
        user_input = int(input("What is n? "))
        if user_input > 0:
            break
    return user_input
        # if n < 0:
        #     continue            # continue to stay in loop
        # else:
        #     break               # break out of loop

def meow(n):
    '''programming convention to start counting by 0'''
    i = 0
    while i < n:
        print("meow")
        i += 1



main()




