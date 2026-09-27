num = [2,34,5,6,657,3,6,9879,45555,436,4]
hight=num[0]
for i in range(0,len(num)):
    if num[i]>=hight:
        s_high=hight
        hight=num[i]
print(hight,"  ",s_high)