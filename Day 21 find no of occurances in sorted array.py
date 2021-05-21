#User function Template for python3
class Solution:
    def first(self,arr,n,x):
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]>x:
                high=mid-1
            elif arr[mid]<x:
                low=mid+1
            else:
                if mid==0 or arr[mid]!=arr[mid-1]:
                    return mid
                else:
                    high=mid-1
        return -1
    def last(self,arr,n,x):
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]>x:
                high=mid-1
            elif arr[mid]<x:
                low=mid+1
            else:
                if mid==n-1 or arr[mid]!=arr[mid+1]:
                    return mid
                else:
                    low=mid+1
        return -1
	def count(self,arr, n, x):
	    ob=Solution()
	    a=ob.first(arr,n,x)
        b=ob.last(arr,n,x)
        if a==-1:
            return 0
        return (b-a)+1
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
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends
