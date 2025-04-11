class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        for num in range(left, right + 1, 1):
            if '0' in str(num):
                continue
            if str(num) == ''.join(d for d in str(num) if num % int(d) == 0):
                l.append(num)
        return l
