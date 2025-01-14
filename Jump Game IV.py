class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N, groups = len(arr), defaultdict(list)
        for i, el in enumerate(arr): 
            groups[el].append(i)
        vis, vis_groups = set(), set()
        def bfs(lvl, dist):
            nextLvl = set()
            for i in lvl:
                if i in vis: continue
                if i == N-1: return dist
                vis.add(i)
                if i: nextLvl.add(i-1)
                if i+1 < N: nextLvl.add(i+1)
                if not arr[i] in vis_groups:
                    vis_groups.add(arr[i])
                    nextLvl.update(groups[arr[i]])
            return bfs(nextLvl, dist + 1)
        return bfs(set([0]), 0)
