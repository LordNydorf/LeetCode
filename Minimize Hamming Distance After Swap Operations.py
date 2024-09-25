from collections import defaultdict
from collections import Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        res = n = len(source)
        G = defaultdict(set)
        for v, w in allowedSwaps:
            G[v].add(w)
            G[w].add(v)
        visited = set()
        def dfs(v, comp):
            visited.add(v)
            comp.append(v)
            for w in G[v]:
                if w not in visited:
                    dfs(w, comp)
        for v in range(n):
            if v in visited: continue
            component = []
            dfs(v, component)
            counts = Counter(source[w] for w in component)
            countt = Counter(target[w] for w in component)
            res -= sum((counts & countt).values())
        return res
