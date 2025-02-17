class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        result = {}
        for c in s:
            if c in result:
                result[c] += 1
            else:
                result[c] = 1
        return set(result.values()) == set([mode(result.values())])
