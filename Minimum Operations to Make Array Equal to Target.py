class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        result = abs(nums[0] - target[0])
        for i in range(1, len(nums)):
            pre, cur = nums[i - 1] - target[i - 1], nums[i] - target[i]
            if (pre > 0 and cur > 0) or (pre < 0 and cur < 0):
                result += max(0, abs(cur) - abs(pre))
            else:
                result += abs(cur)
        return result
