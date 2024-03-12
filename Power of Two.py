class Solution:
    import math
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        a = math.log2(n)
        if a.is_integer():
            return True
        else:
            return False
