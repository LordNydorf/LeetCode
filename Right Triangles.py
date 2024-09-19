class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [0]*m
        cols = [0]*n
        for i in range(m):
            for j in range(n): 
                if grid[i][j]: 
                    rows[i] += 1
                    cols[j] += 1
        ans = 0 
        for i in range(m): 
            for j in range(n): 
                if grid[i][j]:
                    ans += (rows[i]-1)*(cols[j]-1)
        return ans 
