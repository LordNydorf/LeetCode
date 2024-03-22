class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while len(nums) > 0:
            a = min(nums)
            nums.remove(min(nums))
            b = min(nums)
            nums.remove(min(nums))
            arr.append(b)
            arr.append(a)
        return arr
