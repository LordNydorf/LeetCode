class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen, ans, cur = deque(), [], 0
        for num in nums:
            if num != -1:
                seen.appendleft(num)
                cur = 0
                continue
            cur += 1
            ans.append(-1 if cur > len(seen) else seen[cur - 1])
        return ans
