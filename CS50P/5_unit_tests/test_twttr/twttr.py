# test file
VOWELS = {"a", "e", "i", "o", "u",
          "A", "E", "I", "O", "U"}

def main():
    user_input = input("Input: ")
    output = shorten(user_input)
    print("Output:", output)

def shorten(word):
    output_str = ""
    for char in word:
        if char not in VOWELS:
            output_str += char
    return output_str

if __name__ == "__main__":
    main()
