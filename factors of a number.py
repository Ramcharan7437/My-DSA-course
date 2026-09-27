m=int(input("Enter the number :"))
r=[]
for i in range(1,m//2+1):
    if m%i==0:
        r.append(i)
r.append(m)
print(r)
