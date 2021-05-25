#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self,A, N):
        count=0
        res=0
        for i in range(1,N):
            if A[i]>A[i-1]:
                count=count+1
            else:
                res=max(res,count)
                count=0
        return max(res,count)
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
            ob=Solution()
            print(ob.maxStep(A,N))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
