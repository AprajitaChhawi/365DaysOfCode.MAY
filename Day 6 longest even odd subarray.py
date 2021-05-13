def longestevenodd(arr,n):
    count=1
    ma=0
    for i in range(n-2):
        if (arr[i]+arr[i+1])%2==1:
            count=count+1
        else:
            ma=max(ma,count)
            count=1
    if ma==1:
        return 0
    return max(ma,count)
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    m=longestevenodd(l,n)
    print(m)
