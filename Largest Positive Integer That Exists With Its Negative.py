class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        pair = -1
        for num in nums:
            if num > 0 and -num in s:
                pair = max(pair, num)
        return pair
