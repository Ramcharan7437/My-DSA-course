
n = [5,6,7,8,9,0,5,4,6,7,8,2,3,5,7,6]
frequency = {}
for num in n :
    if num in frequency:
        frequency[num]+=1
    else :
        frequency[num] = 1
print(frequency)