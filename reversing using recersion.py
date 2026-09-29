n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
def reverse(left,right):
    if left>right:
        return n
    n[left],n[right]=n[right],n[left]
    reverse(left+1,right-1)
    return n
print(reverse(0,len(n)-1))