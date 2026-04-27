number = int(input("Enter the Number: "))
suum = 0

while number > 0:
    digit = number % 10
    suum = suum + digit
    number = number // 10

print("Sum of digits: ",suum)