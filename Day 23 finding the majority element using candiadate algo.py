class Solution:
    def candidate(self,A,N):
        count=1
        res=0
        for i in range(1,len(A)):
            if A[i]==A[res]:
                count=count+1
            else:
                count=count-1
            if count==0:
                res=i
                count=1
        return res
    def majorityElement(self, A, N):
        if N==0:
            return -1
        if N==1:
            return A[0]
        o=Solution()
        a=o.candidate(A,N)
        count=0
        for i in range(len(A)):
            if A[i]==A[a]:
                count=count+1
        if count>N//2:
            return A[a]
        return -1
        #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
