#User function Template for python3

class Solution:
    def firstIndex(self, arr, n):
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==0:
                low=mid+1
            else:
                if mid==0 or (mid>0 and arr[mid-1]==0):
                    return mid
                high=mid-1
        return -1
    def count1s(self,arr,n):
        o=Solution()
        a=o.firstIndex(arr,n)
        if a==-1:
            return -1
        elif a==n-1:
            return 1
        return (n-1)-a+1
    # Your code goes here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.count1s(a, n))

        T -= 1


if __name__ == "__main__":
    main()
