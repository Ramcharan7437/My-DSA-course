m=int(input("Enter the number :"))
n=m
reverse = 0
while m>0:
    i=m%10
    reverse =reverse*10 +i
    m=m//10
if n==reverse:
    print("it is the palindrome")
else :
    print("it is not the palindrome")