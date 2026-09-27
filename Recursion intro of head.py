count=0
def fun(n):
    global count
    if count==n:
        return
    print("ram")
    count+=1
    fun(n)
n=int(input("hoe many time do you want to print the ram ?"))
fun(n)