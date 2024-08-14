def main():
    user_input = str(input())
    conversion = convert(user_input)
    print(conversion)

def convert(input_string):
    # replace all occurrences of ":)" with the smiling emoji 🙂
    emoji_string = input_string.replace(":)", "\U0001F642")
    # replace all occurrences of ":(" with the frowning emoji 🙁
    emoji_string = emoji_string.replace(":(", "\U0001F641")
    return emoji_string

main()
