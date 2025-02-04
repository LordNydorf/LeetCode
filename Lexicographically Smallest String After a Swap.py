class Solution:
    def getSmallestString(self, s: str) -> str:
        res = [c for c in s]
        for i in range(1, len(s)):
            a, b = int(res[i]), int(res[i - 1])
            if a < b and a % 2 == b % 2:
                res[i], res[i - 1] = res[i - 1], res[i]
                break
        return "".join(res)
