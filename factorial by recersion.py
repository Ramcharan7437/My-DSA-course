def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
m=int(input("Enter the number :"))
print(f"its factorial is {fact(m)}")