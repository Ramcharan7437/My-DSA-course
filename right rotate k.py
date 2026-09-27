m=int(input())
num = [1,3,5,67,8,9,6,5,3,2,4,6]
n=len(num)
k=m%n
temp=num[n-k:]
for i in range(n-k-1,-1,-1):
    num[i+k]=num[i]
num[0:k]=temp
print(num)