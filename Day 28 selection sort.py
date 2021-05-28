#User function Template for python3

class Solution: 
    def select(self, arr, i):
        mid=i
        for j in range(i+1,n):
            if arr[j]<arr[mid]:
                mid=j
        return mid
        # code here 
    
    def selectionSort(self, arr,n):
        for i in range(n):
            j=self.select(arr,i)
            arr[j],arr[i]=arr[i],arr[j]
        return arr
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
