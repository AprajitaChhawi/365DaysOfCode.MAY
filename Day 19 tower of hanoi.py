def hanoi_move ( start , via , target ,n ,k ):
    if k ==2**( n -1):
        print(start,target)
    elif k <2**( n -1):
        return hanoi_move ( start , target , via ,n -1 , k)
    else:
        return hanoi_move ( via , start , target ,n -1 ,k -2**( n -1))
t=int(input())
while t:
    t=t-1
    n,k=map(int,input().split())
    hanoi_move(1,2,3,n,k)

          
