class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [len([i for i in nums1 if i in nums2]) ,len([i for i in nums2 if i in nums1])]
