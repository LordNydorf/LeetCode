class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            lsb = n & 1
            n >>= 1
            result <<= 1
            result |= lsb
        return result
