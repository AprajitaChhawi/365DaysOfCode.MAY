#User function Template for python3

class Solution:
    #Function to find the length of longest subarray of even and odd numbers.
    def maxEvenOdd(self,arr,n):
        ma=1
        co=1
        for i in range(1,n):
            if(arr[i]+arr[i-1])%2!=0:
                co=co+1
            else:
                ma=max(ma,co)
                co=1
        if co==1 and ma==1:
            return 1
        else:
            return max(co,ma)
        #returns: the maximum length
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maxEvenOdd(arr,n))
# } Driver Code Ends
