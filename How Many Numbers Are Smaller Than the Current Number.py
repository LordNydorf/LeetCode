class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smlist = []
        count = 0       
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
                else:
                    continue
            smlist.append(count)
            count = 0
        return smlist
