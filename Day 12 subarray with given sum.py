#User function Template for python3


class Solution:#Function to find a continuous sub-array which adds up to a given number.
    def subArraySum(self,arr, n, s): 
        ch=0
        sa=arr[0]
        i=1
        while i<=n-1:
            while(sa>s and ch<i-1):
                sa=sa-arr[ch]
                ch=ch+1
            if sa==s:
                return ch+1,i
            if i<n:
                sa=sa+arr[i]
            i=i+1
        return -1,-1
    #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
