from heapq import heappush, heappop
class Solution:
    def eatenApples(self, A: List[int], D: List[int]) -> int:
        ans, i, N = 0, 0, len(A)
        h = []
        while i < N or h:
            if i < N and A[i] > 0:
                heappush(h, [i + D[i], A[i]])
            while h and (h[0][0] <= i or h[0][1] <= 0):
                heappop(h)
            if h:
                h[0][1] -= 1
                ans += 1
            i += 1
        return ans 
