try:
    a = int(input("Enter number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Divide by zero error")
except ValueError:
    print("Invalid input")