


class Solution:
    def isfeas(self,arr,n,k,su):
        re=1
        s=0
        for i in range(n):
            if((s+arr[i])>su):
                re=re+1
                s=arr[i]
            else:
                s=s+arr[i]
        return (re<=k)
    #Function to find minimum number of pages.
    def findPages(self,arr, n, m):
        low=max(arr)
        high=sum(arr)
        res=0
        while(low<=high):
            mid=(low+high)//2
            o=Solution()
            if (o.isfeas(arr,n,m,mid)):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
        #code here


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends
