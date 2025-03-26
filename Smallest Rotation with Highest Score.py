class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        diff = [1] * len(nums)
        for i, x in enumerate(nums): 
            diff[(i-x+1) % len(nums)] -= 1
        prefix = list(accumulate(diff))
        return prefix.index(max(prefix))
