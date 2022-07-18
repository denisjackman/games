import re

number = input()
pattern = r"^[189][0-9]"
match = re.match(pattern, number)

if len(number) == 8 and match:
    print("Valid")

else:
    print("Invalid")
