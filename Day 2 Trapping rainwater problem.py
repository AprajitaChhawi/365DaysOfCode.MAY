



class Solution:
    def trappingWater(self, arr,n):
        l=[0]*n
        r=[0]*n
        l[0]=arr[0]
        r[n-1]=arr[n-1]
        pro=0
        for i in range(1,n):
            l[i]=max(l[i-1],arr[i])
        for i in range(n-2,-1,-1):
            r[i]=max(r[i+1],arr[i])
        for i in range(n):
            pro=pro+(min(l[i],r[i])-arr[i])
        return pro
        #Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends
