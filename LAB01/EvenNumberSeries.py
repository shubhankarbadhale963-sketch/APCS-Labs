# user tells whats the end number of even number series should be
n = int(input("Till How Much You Want Even Number Series: "))
print("Even Number Series: ")

#this loop will start from 2 till the user defined number with iteration of +2 
for i in range(2,n+1,2):
    print(i,end =" ")