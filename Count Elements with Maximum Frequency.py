class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        for i in nums:
            hashMap[i] = hashMap[i] + 1
        maxValue = max(hashMap.values())
        count = 0
        for key, value in hashMap.items():
            if value == maxValue:
                count = count + value
        return count
