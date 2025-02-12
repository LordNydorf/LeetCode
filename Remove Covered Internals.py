class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        prevL, prevR = intervals[0]

        res = len(intervals)
        for i in range(1, len(intervals)):
            a, b = intervals[i]
            if a >= prevL and b <= prevR:
                res -= 1
            else:
                prevL, prevR = a, b
        return res
