class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        n = min(steps//2 + 1, arrLen)
        dp = [1] + [0]*n
        for i in range(steps):
            prev = 0
            for j in range(n):
                dp[j], prev = (prev + dp[j] + dp[j + 1], dp[j])
        return dp[0] % (10**9 + 7)
