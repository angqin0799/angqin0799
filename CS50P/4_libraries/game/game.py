import random


while True:
    try:
        level = int(input("Level: "))
    except (ValueError, NameError):
        pass
    else:
        if level > 0:
            right_guess = random.randint(1, level)
            # print(right_guess)
            while True:
                try:
                    guess = int(input("Guess: "))
                except ValueError:
                    pass
                else:
                    if guess > right_guess:
                        print("Too large!")
                    elif guess < right_guess:
                        print("Too small!")
                    else:
                        print("Just right!")
                        break
            break
        else:
            pass



