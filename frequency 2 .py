n=[5,45,6,7,7,8,8,4,55,54,43,534,5,7,7,0,7,4,5,64,654,46,6]
hashmap={}
for num in n :
    hashmap[num]=hashmap.get(num,0)+1
print(hashmap)