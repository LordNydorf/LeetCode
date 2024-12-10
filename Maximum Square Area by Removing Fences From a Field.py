class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 10 ** 9 + 7
        hFences += [1, m]
        vFences += [1, n]
        hFences.sort()
        vFences.sort()
        seen = set()
        res = 0
        for i in range(len(hFences) - 1):
            for j in range(i + 1, len(hFences)):
                seen.add(hFences[j] - hFences[i])
        for i in range(len(vFences) - 1):
            for j in range(i + 1, len(vFences)):
                if vFences[j] - vFences[i] in seen:
                    res = max(res, ((vFences[j] - vFences[i]) * (vFences[j] - vFences[i])))
        return res % mod if res != 0 else -1
