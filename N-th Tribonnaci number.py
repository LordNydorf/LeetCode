class Solution:
    def tribonacci(self, n: int, memo = {}) -> int:
        if n in memo:
            return memo[n]
        if n < 2:
            return n
        elif n == 2:
            return 1
        else:
            memo[n] = self.tribonacci(n-3)+self.tribonacci(n-2)+self.tribonacci(n-1)
            return memo[n]
