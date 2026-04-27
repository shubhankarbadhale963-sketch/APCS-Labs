a = 0
b = 1
fib = 0

# user decide how many numbers series he wants
n = int(input("Enter how many Numbers you want: "))

for i in range(n):
    print(a)                
    fib = a + b         
    a = b               
    b = fib             