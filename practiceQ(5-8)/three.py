import re

password = input("Enter password: ")

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

if re.match(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")

