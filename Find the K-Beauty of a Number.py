class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        numStr = str(num)
        n = len(numStr)
        for i in range(n - k + 1):
            subStr = numStr[i : i + k]
            divisor = int(subStr)
            if divisor != 0 and num % divisor == 0:
                res += 1
        return res
