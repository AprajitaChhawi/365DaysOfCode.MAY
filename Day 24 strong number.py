#User function Template for python3

class Solution:
    def fact(self,n):
        fac=1
        for i in range(2,n+1):
            fac=fac*i
        return fac
    def isStrong(self, N):
        s=0
        num=N
        while(num!=0):
            temp=num%10;
            s=s+ob.fact(temp)
            num=int(num/10)
        if(N==s):
            return 1
        else:
            return 0
        
        # code here 
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        ob = Solution()
        print(ob.isStrong(N))
# } Driver Code Ends
