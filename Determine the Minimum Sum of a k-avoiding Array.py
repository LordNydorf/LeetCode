class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        used = set()
        index = 0
        while len(used) < n:
            index += 1
            if k - index not in used:
                used.add(index)
        return sum(used)
