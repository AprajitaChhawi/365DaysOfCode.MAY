#User function Template for python3

##Complete this function
def leftIndex(N, arr, X):
    low=0
    high=N-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>X:
            high=mid-1
        elif arr[mid]<X:
            low=mid+1
        else:
            if mid==0 or arr[mid]!=arr[mid-1]:
                return mid
            else:
                high=mid-1
    return -1
    #Your code here
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            x=int(input())
            
            print(leftIndex(N,A,x))
            
            
            T-=1


if __name__ == "__main__":
    main()
    
    
# } Driver Code Ends
