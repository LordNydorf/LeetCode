from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = Counter(arr)
        s = set()
        for i in h:
            if h[i] in s:
                return False
            s.add(h[i])
        return True
