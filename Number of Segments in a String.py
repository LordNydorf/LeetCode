class Solution:
    def countSegments(self, s: str) -> int:
        result = s.split()
        count = 0
        for _ in result:
            count += 1
        return count
