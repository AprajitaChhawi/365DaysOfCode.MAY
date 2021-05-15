def printgroups(arr,n):
    for i in range(1,n):
        if(arr[i]!=arr[i-1]):
            if (arr[i]!=arr[0]):
                print(i,end=" ")
            else:
                print(i-1)
    if(arr[n-1]!=arr[0]):
        print(n-1)
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    printgroups(l,n)
