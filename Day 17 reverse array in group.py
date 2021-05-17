#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k
    def reverse(self,arr,start,end):
        while(start<end):
            arr[start],arr[end]=arr[end],arr[start]
            start=start+1
            end=end-1
	def reverseInGroups(self, arr, N, K):
	    d=0
	    while(d+K<N):
	        self.reverse(arr,d,d+K-1)
	        d=d+K
	    self.reverse(arr,d,N-1)
		# code here

#{ 
#  Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends
