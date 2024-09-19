class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_mean(nums):
            mid = int(len(nums)/2)
            if len(nums)%2==0:
                return (nums[mid]+nums[mid-1])/2
            else:
                return nums[mid]/1   
        l1= len(nums1)
        l2= len(nums2)
        final_num = [0]*int(((l1+l2)/2)+1)
        mid = len(final_num)
        if l1==0:
            return find_mean(nums2)
        if l2==0:
            return find_mean(nums1)
        i,j,k=0,0,0
        while k<mid:
            if   i<l1 and (j>=l2 or nums1[i]<=nums2[j]):
                final_num[k]=nums1[i]
                i+=1
                k+=1
            elif j<l2 and (i>=l1 or nums2[j]<=nums1[i]):
                final_num[k]=nums2[j]
                j+=1
                k+=1
        if (l1+l2)%2==0:
            return sum(final_num[-2:])/2
        else: return sum(final_num[-1:])/1