n=input("enter the no")
num=int(n[::-1])
while num > 0:
    m=num%10
    print(m)
    num=num//10