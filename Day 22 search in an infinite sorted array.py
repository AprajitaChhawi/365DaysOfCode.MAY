def Bsearch(arr,n,start,end,x):
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return -1
def search(arr,n,x):
    if arr[0]==x:
        return 0
    i=1
    while(arr[i]<x):
        i=i*2
    if(arr[i]==x):
        return i
    return Bsearch(arr,n,(n//2)+1,n-1,x)
t=int(input())
while t:
    t=t-1
    n=int(input())
    arr=list(map(int,input().split()))
    x=int(input())
    a=search(arr,n,x)
    print(a)
