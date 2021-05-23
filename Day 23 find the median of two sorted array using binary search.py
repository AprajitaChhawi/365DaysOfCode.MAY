#User function Template for python3
from sys import maxsize
class Solution:
    
    #Function to find the median of the two arrays when they get merged.
    def findMedianSortedArrays(self,arr1, n1, arr2, n2):
       low=0
       high=n1
       while(low<=high):
            i1=(low+high)//2
            i2=((n1+n2+1)//2)-i1
            if i1==n1:
                min1=999999
            else:
                min1=arr1[i1]
            if i1==0:
                max1=-999999
            else:
                max1=arr1[i1-1]
            if i2==n2:
                min2=999999
            else:
                min2=arr2[i2]
            if i2==0:
                max2=-999999
            else:
                max2=arr2[i2-1]
            if(max1<=min2 and max2<=min1):
                if (n1+n2)%2==0:
                    return (max(max1,max2)+min(min1,min2))//2
                else:
                    return max(max1,max2)
            elif max1>min2:
                high=i1-1
            else:
                low=i1+1
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n1,n2=list(map(int,(input().split())))
        arr1=list(map(int,(input().split())))
        arr2=list(map(int,(input().split())))
        
        if n1<n2:
            print(Solution().findMedianSortedArrays(arr1,n1, arr2,n2))
        else:
            print(Solution().findMedianSortedArrays(arr2,n2, arr1,n1))
# } Driver Code Ends
