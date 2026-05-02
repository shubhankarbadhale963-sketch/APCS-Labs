def adding(a):
    summ = 0
    for i in range(len(a)):
        summ += a[i]
    return(summ)

lis = [10, 20, 30, 40]
print(adding(lis))