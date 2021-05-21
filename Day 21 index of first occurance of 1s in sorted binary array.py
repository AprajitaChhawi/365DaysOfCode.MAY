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
        print(ob.firstIndex(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
