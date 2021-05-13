#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def kadane(arr,n):
    if n==1:
        return arr[0]
    if max(arr)<0:
        return max(arr)
    curr=0
    ma=0
    for i in range(n):
        curr=curr+arr[i]
        if (curr>ma):
            ma=curr
        elif curr<0:
            curr=0
    return ma
def circularSubarraySum(arr,n):
    a1=kadane(arr,n)
    if a1<0:
        return a1
    arrsum=0
    for i in range(n):
        arrsum=arrsum+arr[i]
        arr[i]=-arr[i]
    a2=arrsum+kadane(arr,n)
    return max(a1,a2)
    
    ##Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math
import sys

    
    

if __name__ == "__main__":
    T=int(input())
    while(T>0):
            
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
            
        print(circularSubarraySum(arr,n))
        
        T-=1
    
# } Driver Code Ends
