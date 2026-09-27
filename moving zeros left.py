m=[1,0,7,0,5,0,4,8,6,4,0,0,0,7,5,7]
i=0
n=int(len(m))
a=n
while i< n:
    if m[i]==0:
       del m[i]
       n=int(len(m))
    else:
        i+=1
m=m+[0]*(a-n)
print(m)