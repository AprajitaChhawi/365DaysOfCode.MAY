#User function Template for python3


class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr,low,high):
        n=high-low
        while(low<=high):
            mid=(low+high)//2
            if mid>0 and arr[mid]<arr[mid-1]:
                return arr[mid]
            elif arr[mid]>=arr[low] and arr[mid]>arr[high]:
                low=mid+1
            else:
                high=mid-1
        return arr[low]
            
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
            obj = Solution()
            print(obj.minNumber(A,0,N-1))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
