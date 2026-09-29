n=[1,1,1,1,0,1,1,1,0,1,1,0,1,1,1]
count=0
max_count=0
m=len(n)
for i in range(0,m):
    if n[i]==1:
        count+=1
    else:
        max_count=max(count,max_count)
        count=0
print(max(count,max_count))