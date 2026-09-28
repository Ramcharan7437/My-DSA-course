def sum(Sum,i,n):
    if i==n:
        print(Sum)
        return
    sum(Sum+i,i+1,n)
m=int(input("Enter the number :"))
sum(0,1,m)
print(sum)
    