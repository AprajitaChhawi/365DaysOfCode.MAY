#User function Template for python3

class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        while(l<=h):
            mid=(l+h)//2
            if A[mid]==key:
                return mid
            elif A[mid]>A[l]:
                if(key>=A[l] and key<A[mid]):
                    h=mid-1
                else:
                    l=mid+1
            else:
                if (key<=A[h] and key>A[mid]):
                    l=mid+1
                else:
                    h=mid-1
        return -1
        # Complete this function

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends
