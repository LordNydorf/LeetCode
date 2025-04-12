class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos = {ch : i for i, ch in enumerate(t)}
        return sum([abs(i - pos[s[i]]) for i in range(len(s))])
