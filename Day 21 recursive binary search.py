#User function template for Python

class Solution:
    def bs(self,arr,low,high,k):
        if(low>high):
            return -1
        mid=(low+high)//2
        o=Solution()
        if arr[mid]==k:
            return mid
        elif (arr[mid]>k):
            return o.bs(arr,low,mid-1,k)
        else:
            return o.bs(arr,mid+1,high,k)
	def binarysearch(self, arr, n, k):
	    ob=Solution()
	    a=ob.bs(arr,0,n-1,k)
	    if a==None:
	        return -1
	    return a
		# code here

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends
