#{ 
#Driver Code Starts
#Initial Template for Python 3


# Python3 implementation of the approach 


 # } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to return the maximum water that can be stored.
    def maxWater(self, height, n):
        low=0
        high=n-1
        cur=0
        while(low<=high):
            if height[low]<height[high]:
                cur=max(cur,(high-low-1)*height[low])
                low=low+1
            else:
                cur=max(cur,(high-low-1)*height[high])
                high=high-1
        return cur
        #Your code here
     

#{ 
#Driver Code Starts.


def main():
    t=int(input())
    while(t>0):
        n=int(input())
        height=[int(x) for x in input().strip().split()]
        ob=Solution()
        print (ob.maxWater(height, n));
        t-=1

if __name__ == "__main__":
    main()
#} Driver Code Ends
