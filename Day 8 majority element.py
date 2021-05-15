class Solution:
    def majorityElement(self, A, N):
        d={}
        for i in A:
)))0))
if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for i in d.keys():
            if d[i]>N//2:
                return i
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
