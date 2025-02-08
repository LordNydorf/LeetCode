class Solution:
    def maxScore(self, nums: List[int]) -> int:
        return sum(n > 0 for n in accumulate(sorted(nums, reverse = True)))
