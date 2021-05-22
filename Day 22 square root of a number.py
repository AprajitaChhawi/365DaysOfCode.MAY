#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x):
        low=1
        high=x
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            ms=mid*mid
            if(ms==x):
                return mid
            elif(ms>x):
                high=mid-1
            else:
                low=mid+1
                ans=mid
        return ans
    #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
