m=[1,3,6,8,0,3,3,1,4,6,8,9,54,3,5]##give any number of element in any number of times
f={}
for i in m:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)