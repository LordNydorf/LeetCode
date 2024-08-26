class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_so_far = max_overall = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                max_so_far += nums[i]
                max_overall = max(max_overall, max_so_far)
            else: 
                max_so_far = nums[i]
        return max_overall   
