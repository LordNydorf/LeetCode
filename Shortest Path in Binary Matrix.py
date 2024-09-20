class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        if grid[0][0] == 1 or grid[n][n] == 1: return -1
        if len(grid) == 1: return 1
        q, level = deque([(0,0)]), 2
        while q:
            for _ in range(len(q)):
                pr, pc = q.popleft()
                for (x,y) in ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)):
                    r, c = pr + x, pc + y
                    if r<0 or r>n or c<0 or c>n or grid[r][c] != 0:
                        continue
                    if r == n and c == n: return level
                    grid[r][c] = 2
                    q.append((r, c))
            level += 1
        return -1
