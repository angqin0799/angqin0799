import validators

email_input = input("What's your email address? ")

if validators.email(email_input):
    print("Valid")
else:
    print("Invalid")
