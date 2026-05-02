#Write a Python program to validate a phone number using regular expressions. The phone number must contain exactly 10 digits. 
import re

phone = input("Enter the Phone Number: ")

pattern = r'^\d{10}$'

if re.match(pattern,phone):
    print("Valid Phone Number")
else:print("Invalid")