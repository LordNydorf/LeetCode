from collections import Counter
class Solution:    
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for i in count.values():
            return all(i % 2 == 0 for i in Counter(nums).values())
