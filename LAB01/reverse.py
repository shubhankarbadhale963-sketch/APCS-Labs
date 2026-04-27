number = int(input("Enter the Number: "))
reverse = 0

while number > 0:
    digit = number % 10       # get last digit
    reverse = reverse * 10 + digit
    number = number // 10     # remove last digit

print("Reversed number:", reverse)