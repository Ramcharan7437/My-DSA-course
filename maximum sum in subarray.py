n=[1,4,-3,7,5,-3,-4,5,7,9,-6]
total=0
maxi=float("-inf")
for i in range(0,len(n)):
    total=total+n[i]
    maxi=max(maxi,total)
    if total<0:
        total=0
print(maxi)
