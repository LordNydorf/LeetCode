class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        m = max(nums)
        for x in range(1, m+1): 
            g = 0
            for xx in range(x, m+1, x): 
                if xx in nums: 
                    g = gcd(g, xx)
            if g == x: ans += 1
        return ans 
