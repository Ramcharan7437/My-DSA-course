n=[5,6,8,9,5,6,3,2,6,7,9,0,6,4,3,0,2,2,3,5,6,8,9,4]
m=[453,45,56,567,7,7,4,8,8,9,46,34,3]
hashmap=[0]*11
for num in n:
    hashmap[num]+=1
for num in m:
    if num<1 or num>10:
        print(num,":",0)
    else:
        print(num,":",hashmap[num])


   


