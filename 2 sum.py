num=[1,2,3,5,7,9,5,3,7,8,9,3,0,3]
f={}
target=int(input("Enter the target"))
for i in range(0,len(num)):
    need=target-num[i]
    if need in f:
        print(f[need],",",i)
     
    f[num[i]]=i