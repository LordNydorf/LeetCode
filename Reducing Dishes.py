class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        res = cnt = 0
        while satisfaction:
            cur = satisfaction.pop()
            if cur + cnt < 0: return  res
            cnt += cur
            res += cnt
        return res
