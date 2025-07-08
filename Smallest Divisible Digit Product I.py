class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        num = n
        while True:
            tmp = num
            prodModul = 1
            while tmp:
                dig = tmp % 10
                if dig == 0:
                    prodModul = 0
                    break
                prodModul = (prodModul * dig) % t
                tmp //= 10
            if prodModul == 0:
                return num
            num += 1
