class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        set1 = set(fronts + backs)
        for f,b in zip(fronts, backs):
            if f == b:
                set1.discard(f)
        return min(set1, default = 0)
