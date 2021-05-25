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
    #Function to find repeated element and its frequency.
    def findRepeating(self,arr,n):
        temp=arr[0]
        slow=arr[temp]
        fast=arr[arr[temp]]
        while(slow!=fast):
            slow=arr[slow]
            fast=arr[arr[fast]]
        slow=arr[0]
        while(slow!=fast):
            slow=arr[slow]
            fast=arr[fast]
        repeat=slow
        o=Solution()
        a=o.first(arr,n,repeat)
        if a==-1:
            return -1,-1
        else:
            return repeat,o.last(arr,n,repeat)-a+1
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = list((map(int,input().strip().split())))
        
        ans=Solution().findRepeating(arr,n)
        print(ans[0],ans[1])
        
        
# } Driver Code Ends
