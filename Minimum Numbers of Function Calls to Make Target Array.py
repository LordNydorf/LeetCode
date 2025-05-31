class Solution:
    def minOperations(self, nums: List[int]) -> int:
        add = multiply = 0
        for num in nums:
            add += bin(num).count('1')
            if num > 0:
                multiply = max(multiply, num.bit_length() - 1)
        return add + multiply
