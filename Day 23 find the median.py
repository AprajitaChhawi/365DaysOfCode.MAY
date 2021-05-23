#User function Template for python3

class Solution:
	def find_median(self, v):
	    v.sort()
	    a=len(v)
	    if a%2==0:
	        return (v[a//2]+v[(a//2)-1])//2
	    else:
	        return v[a//2]
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends
