class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        l = len(n)
        if l < 4:
            return n
        result = ""
        n = n[::-1]
        for i in range(l):
            if not i % 3 and i != 0:
                result += "."
            result += n[i]
        return result[::-1]
