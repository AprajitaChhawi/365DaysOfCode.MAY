def longest(l):
    count=0
    ma=0
    for i in l:
        if(i>=0):
            count=count+1
        elif(i<0):
            if(ma<count):
                ma=count
            count=0
    print(max(ma,count))        
try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=list(map(int,input().split()))
        if(max(l)<0):
            print(0)
        else:
            longest(l)
except Exception:
    pass;
            
            
            
