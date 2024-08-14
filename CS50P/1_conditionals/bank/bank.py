
greeting = str(input("Greeting: "))

processed_greeting = greeting.strip().lower()

if "hello" in processed_greeting:                       
    print("$0")
elif processed_greeting.startswith("h") == True:
    print("$20")
else:
    print("$100")


