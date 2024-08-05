class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = num[::-1]
        s = int(num)
        k = str(s)
        k = k[::-1]
        return k
