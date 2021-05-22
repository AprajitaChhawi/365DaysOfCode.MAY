#User function Template for python3
class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
	    d={}
	    for i in arr:
	        if i not in d:
	            d[i]=1
	        else:
	            d[i]=d[i]+1
	    for i in arr:
	        if x-i==i:
	            if d[i]>1:
	                return True
	        elif x-i in d:
	            return True
	    return False
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends
