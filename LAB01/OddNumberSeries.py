# user tells whats the end number of Odd number series should be
n = int(input("Till How Much You Want Odd Number Series: "))
print("Odd Number Series: ")

#this loop will start from 1 till the user defined number with iteration of +2 
for i in range(1,n+1,2):
    print(i,end =" ")