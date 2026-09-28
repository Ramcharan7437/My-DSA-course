n=int(input("from which number it what to start"))
m=int(input("Enter the number up to  :"))

def num(a,b):
    if a>b:
        return
    print(a)
    num(a+1,b)
num(n,m)