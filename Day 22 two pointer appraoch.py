def tpa(arr,n,x):
    l=0
    r=n-1
    while(l<r):
        s=arr[l]+arr[r]
        if s==x:
            return l,r
        elif s>x:
            r=r-1
        else:
            l=l+1
    return 0,0
t=int(input())
while t:
    t=t-1
    n=int(input())
    arr=list(map(int,input().split()))
    x=int(input())
    a,b=tpa(arr,n,x)
    if a==0 and b==0:
        print(-1)
    print(a,b)
