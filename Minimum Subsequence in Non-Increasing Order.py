class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        total = sum(nums)
        sub = 0
        for i in range(0, len(nums) + 1):
            if sub > total-sub:
                break
            sub += nums[i]
        return nums[:i]
