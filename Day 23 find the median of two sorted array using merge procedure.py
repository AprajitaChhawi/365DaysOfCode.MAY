#User function Template for python3

class Solution:
    
    #Function to find the median of the two arrays when they get merged.
    def findMedianSortedArrays(self,arr1, n1, arr2, n2):
        n=n1+n2
        if n1==0 or n2==0:
            return 0
        l=[]
        i=0
        j=0
        while(i!=n1 and j!=n2):
            if arr1[i]<arr2[j]:
                l.append(arr1[i])
                i=i+1
            elif arr1[i]>arr2[j]:
                l.append(arr2[j])
                j=j+1
            else:
                l.append(arr1[i])
                l.append(arr2[j])
                i=i+1
                j=j+1
        if i!=n1:
            l.extend(arr1[i:n1])
        if j!=n2:
            l.extend(arr2[j:n2])
        if n%2==0:
            return (l[n//2]+l[(n//2)-1])//2
        else:
            return l[n//2]
       
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
