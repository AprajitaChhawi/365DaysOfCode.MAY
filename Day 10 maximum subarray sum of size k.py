#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        if K>N:
            return -1
        ma=0
        s=0
        for i in range(K):
            s=s+Arr[i]
        ma=s
        for i in range(K,N):
            s=s+Arr[i]-Arr[i-K]
            ma=max(ma,s)
        return ma
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends
