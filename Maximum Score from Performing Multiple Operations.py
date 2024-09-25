class Solution:
    def maximumScore(self, nums: List[int], muls: List[int]) -> int:
        n, m = len(nums), len(muls)
        @lru_cache(2000)
        def dp(l, i):
            if i == m: return 0
            pickLeft = dp(l+1, i+1) + nums[l] * muls[i]
            pickRight = dp(l, i+1) + nums[n-(i-l)-1] * muls[i]
            return max(pickLeft, pickRight)
        return dp(0, 0)
