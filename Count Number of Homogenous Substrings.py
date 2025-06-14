class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        res = 0
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                res += count * (count + 1) // 2
                count = 1
        res += count * (count + 1) // 2
        return res % mod
