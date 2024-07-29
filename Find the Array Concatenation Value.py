class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i = 0
        c = 0
        j = len(nums) - 1
        while(i <= j):
            if(i == j):
                c += nums[i]
                break
            s = str(nums[i]) + str(nums[j])
            c += int(s)
            i += 1
            j -= 1
        return c
