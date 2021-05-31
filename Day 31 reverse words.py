try:
    t=int(input())
    while t:
        t=t-1
        l=input().split(".")
        l1='.'.join(reversed(l))
        print(l1)
except Exception:
    pass;

