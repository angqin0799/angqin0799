import random


def main():
    level = get_level()
    total_points = 0

    for _ in range(10):
        x, y = generate_integer(level)
        z = x + y

        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == z:
                    total_points += 1
                    break
                else:
                    print("EEE")
            except (ValueError, UnboundLocalError):
                print("EEE")
                pass

        else:
            print(f"{x} + {y} = {z}")

    print("Score:", total_points)



def get_level():
    while True:
        try:
            level_input = int(input("Level: "))
            if 1 <= level_input <= 3:
                return level_input
            else:
                continue
        except ValueError:
            pass



def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y




if __name__ == "__main__":
    main()
