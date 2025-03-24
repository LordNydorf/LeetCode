class Solution:
    def integerBreak(self, n: int) -> int:
        max_product = 0
        for k in range(2, n + 1):
            low: int = n // k
            high = low + 1
            b = n - k * low
            a = k - b
            max_product = max(max_product, low ** a * high ** b)
        return max_product
