try:
    t=int(input())
    while t:
        t=t-1
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        for i in set(l):
            if(l.count(i)==1):
                print(i)
except Exception:
    pass;
