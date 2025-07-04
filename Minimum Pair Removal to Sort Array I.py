from typing import List
class Solution:
    def isNondecreasing(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        while not self.isNondecreasing(nums):
            min_sum = float('inf')
            index = -1
            for i in range(len(nums) - 1):
                sum_pair = nums[i] + nums[i + 1]
                if sum_pair < min_sum:
                    min_sum = sum_pair
                    index = i
            temp = []
            i = 0
            while i < len(nums):
                if i == index:
                    temp.append(nums[i] + nums[i + 1])
                    i += 2  
                else:
                    temp.append(nums[i])
                    i += 1
            nums = temp
            ops += 1
        return ops
