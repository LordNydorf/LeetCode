class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def generateSums(arr):
            sums = set()
            n = len(arr)
            for i in range(n + 1):
                for comb in combinations(arr, i):
                    sums.add(sum(comb))
            return list(sums)
        mid = len(nums) // 2
        firstHalf = nums[:mid]
        secondHalf = nums[mid:]
        sums1 = generateSums(firstHalf)
        sums2 = generateSums(secondHalf)
        sums2.sort()
        result = float('inf')
        for s1 in sums1:
            target = goal - s1
            idx = bisect_left(sums2, target)
            if idx < len(sums2):
                result = min(result, abs(s1 + sums2[idx] - goal))
            if idx > 0:
                result = min(result, abs(s1 + sums2[idx - 1] - goal))
        return result
