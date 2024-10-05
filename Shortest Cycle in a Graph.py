class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        ans = math.inf
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(curr,par,dist):
            nonlocal ans
            if curr in hmap and hmap[curr][1] == 1:
                ans = min(ans,dist - hmap[curr][0])
                return
            vis.add(curr)
            hmap[curr] = [dist,1]
            for it in graph[curr]:
                if it != par and (it not in hmap or hmap[it][0] > dist + 1 or hmap[it][1] == 1):
                    dfs(it,curr,dist+1)
            hmap[curr] = [dist,0]
            return
        vis = set()
        for i in range(n):
            if i not in vis:
                hmap = defaultdict(list)
                dfs(i,-1,0)  
        if ans == math.inf:
            return -1
        else:
            return ans
