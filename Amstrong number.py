m=int(input("Enter the number :"))
n=m
amstrong = 0

while m>0:
    i=m%10
    amstrong=amstrong + i**3
    m = m//10
if 0<=n<10:
    amstrong=n
if n==amstrong:
    print("it is the amstrong number")
else:
    print("it is not the amstrong number")