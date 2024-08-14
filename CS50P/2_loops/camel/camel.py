
def main():
    camel_input = input("camelCase: ")
    snake_output = camel_to_snake(camel_input)
    print("snake_case:", snake_output)


def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            # Concatenate underschoor before uppercase characters
            snake_case += "_" + char
        else:
            # Append each character characters to snake_case variable
            snake_case += char
    return snake_case.lstrip("_").lower()

main()
