class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        maxi = max(nums) + 1
        dic = {}
        prefix=[0]*maxi
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in range(1,maxi):
            if i not in dic:
                prefix[i] = prefix[i-1]
            else:
                prefix[i] = prefix[i-1]+dic[i]
        sumP = 0
        for i in set(nums):
            for j in range(i,maxi,i):
                sumP += dic[i]*(prefix[-1]-prefix[j-1])
        return sumP % (10**9 +7)
