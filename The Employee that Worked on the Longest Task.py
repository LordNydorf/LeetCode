class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        sum = 0
        for i in range(1, len(logs)):
            sum += logs[i-1][1]
            logs[i][1] -= sum
        logs.sort()
        maxWork = logs[0][0]
        longestWork = logs[0][1]
        for i in range(1, len(logs)):
            if longestWork < logs[i][1]:
                longestWork = logs[i][1]
                maxWork = logs[i][0]
        return maxWork
