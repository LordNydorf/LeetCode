class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        for p in range(int(log2(n)), 1, -1): 
            k = int(n**(1/p))
            if (k**(p+1)-1)//(k-1) == n: return str(k)
        return str(n-1)
