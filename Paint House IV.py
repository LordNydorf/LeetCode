class Solution:
    def minCost(self, n, cost):
        n = len(cost)
        @lru_cache(None)
        def function(i,prev_color,last_color):
            if i >= n//2:
                return 0 
            min_cost = float("inf")
            for j in range(3):
                for k in range(3):
                    if j != prev_color and j != k and k != last_color:
                        min_cost = min(min_cost,cost[i][j]+cost[n-1-i][k]+function(i+1,j,k))
            return min_cost 
        return function(0, -1, -1)
