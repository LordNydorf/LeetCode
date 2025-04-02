class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_less = 0
        sum_greater = 0
        for e in nums:
            if e < 10:
                sum_less += e
            else:
                sum_greater += e
        if sum_less == sum_greater:
            return False
        return True
