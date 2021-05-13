#User function Template for python3


class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        count=0
        maxc=0
        while(N!=0):
            if(N%2==1):
                count=count+1
            else:
                maxc=max(maxc,count)
                count=0
            N=N//2
        return max(maxc,count)
            
        ##Your code here




#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math





def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        obj = Solution()
        print(obj.maxConsecutiveOnes(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
