class Solution:
    def maxJump(self, a: List[int]) -> int:
        return max([a[1] - a[0], *map(sub, a[2 : ], a)])
