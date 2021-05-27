#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
        l=[]
        prime=[True for i in range(N+1)]
        p=2
        while(p*p<=N):
            if(prime[p]==True):
                for i in range(p*p,N+1,p):
                    prime[i]=False
            p=p+1
        for j in range(2,N+1):
            if prime[j]:
                print(j)
                
            
    	#code here 



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        print()
# } Driver Code Ends
