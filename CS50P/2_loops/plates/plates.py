
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")








def is_valid(s):

    if not start_with_two_letters(s):
        return False

    if not valid_length(s):
        return False

    if sandwich_numbers(s):
        return False

    if zero_first(s):
        return False

    if non_alphanumeric(s):
        return False

    return True








def valid_length(s):
    ''' verify plates must contain min to max characters '''
    min_char = 2
    max_char = 6
    return min_char <= len(s) <= max_char


def start_with_two_letters(s):
    ''' verify plates must start with at least two letters '''
    alpha_counter = 0
    for char in s:
        if char.isalpha():
            alpha_counter += 1
            if alpha_counter >= 2:
                return True
    return False


def zero_first(s):
    ''' detects if first number used is a zero '''
    digit_counter = 0
    for char in s:
        if char.isdigit():
            digit_counter += 1
            if digit_counter == 1 and char == '0':
                return True
    return False


def sandwich_numbers(s):
    ''' detects if a number comes before a letter '''
    digit_found = False
    then_alpha_found = False

    for char in s:
        if char.isdigit():
            digit_found = True
        elif char.isalpha() and digit_found:
            then_alpha_found = True
            break
    return digit_found and then_alpha_found


def non_alphanumeric(s):
    ''' detects if any characters are non-alphanumeric '''
    for char in s:
        if char.isalnum() == False:
            return True
    return False








main()
