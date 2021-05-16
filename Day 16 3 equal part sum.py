def findsplit(arr,n):
    presum=0
    ind1=-1
    ind2=-1
    s=arr[0]
    for i in range(1,n):
        s=s+arr[i]
    if s%3!=0:
        return 0,0
    s1=s//3
    s2=2*s1
    for i in range(n):
        presum=presum+arr[i]
        if presum==s1 and ind1==-1:
            ind1=i
        elif presum==s2 and ind2==-1:
            ind2=i
    if ind1!=-1 and ind2=-1:
        return ind1,ind2
    return 0,0
t=int(input())
while t:
    t=t-1
    n=int(input())
    arr=list(map(int,input().split()))
    a,b=findsplit(arr,n)
    print(a,b)
