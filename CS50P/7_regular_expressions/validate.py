import re

email = input("What's your email? ").strip()
# re.search(pattern, string, flags=0)
# re.match
# re.fullmatch
# .* zero or more reps of any character
# [^@] any char except an @ sign "complement"
# [a-zA-Z0-9_] == \w
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
