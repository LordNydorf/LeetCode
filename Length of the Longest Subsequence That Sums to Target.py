class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        (dp:= [0]).extend([-1] * target)
        for num in nums:
            for i in reversed(range(num, target+1)):
                nxt = dp[i - num] + 1
                dp[i] = max(nxt, dp[i]) if nxt else dp[i]
        return dp[-1]
