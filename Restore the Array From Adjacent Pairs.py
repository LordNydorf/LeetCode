class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = defaultdict(set)
        for u, v in adjacentPairs:
            d[u].add(v)
            d[v].add(u)
        for u, nbr_u in d.items():
            if len(nbr_u) == 1:
                break
        ans = [u]
        prev_u = None
        n = len(adjacentPairs) + 1
        while len(ans) < n:
            for v in d[u]:
                if v != prev_u:
                    ans.append(v)
                    prev_u = u
                    u = v
                    break
        return ans
