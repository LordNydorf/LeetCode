class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i <= n:
            if i in nums:
                i += 1
            else:
                return i
