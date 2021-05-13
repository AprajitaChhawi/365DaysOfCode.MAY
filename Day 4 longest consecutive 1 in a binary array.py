def consecutive(a,n):
    count=0
    maxc=0
    for i in a:
        if i==1:
            count=count+1
        else:
            maxc=max(maxc,count)
            count=0
    return max(maxc,count)
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    m=consecutive(l,n)
    print(m)
