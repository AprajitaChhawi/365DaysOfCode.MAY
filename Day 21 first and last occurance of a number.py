#User function Template for python3
def first(arr,n,x):
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            if mid==0 or arr[mid]!=arr[mid-1]:
                return mid
            else:
                high=mid-1
    return -1
def last(arr,n,x):
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            if mid==n-1 or arr[mid]!=arr[mid+1]:
                return mid
            else:
                low=mid+1
    return -1
def find(arr,n,x):
    a=first(arr,n,x)
    b=last(arr,n,x)
    return a,b
    # code here


#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends
