
user_input = str(input("What is the Answer to the Great Question of Life, the Universe, and Everthing? "))

processed_input = user_input.strip().lower().replace("-"," ")

if processed_input == "42" or processed_input == "forty two":
    print("Yes")
else:
    print("No")






