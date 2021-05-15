#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def reverse(self,A,low,high):
        while(low<high):
            A[low],A[high]=A[high],A[low]
            low=low+1
            high=high-1
    def rotateArr(self,A,D,N):
        ob=Solution()
        ob.reverse(A,0,D-1)
        ob.reverse(A,D,N-1)
        ob.reverse(A,0,N-1)
        
        #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
