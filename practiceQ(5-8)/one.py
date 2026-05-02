# Write a Python program to validate an email address using regular expressions. The 
# program should check whether the given email is valid or not

import re

email = input("Enter the Email: ")

pattern = r'^[\w\.]+@[\w\.]+\.\w+$'

if re.match(pattern , email ):
    print("Valid Email")
else:
    print("Invalid email")