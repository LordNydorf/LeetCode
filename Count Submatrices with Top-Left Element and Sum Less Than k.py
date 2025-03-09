class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        grid = map(accumulate, grid)
        grid = map(accumulate, zip(*grid))
        return sum(map(lambda x: x <= k, chain(*grid)))
