class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        lst = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        for i in range(len(even)):
            lst.append(even[i])
            lst.append(odd[i])
        return lst
