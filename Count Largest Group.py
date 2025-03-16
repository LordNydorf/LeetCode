class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1, n + 1):
            t = sum(map(int, list(str(i))))
            d[t] = d.get(t, 0) + 1
        return sum(1 for i in d.values() if i >= max(d.values()))
