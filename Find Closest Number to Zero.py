class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        if not nums: return 0
        closest = nums[0]
        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and  num > closest):
                closest = num
        return closest
