class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        X = list(Counter(nums).values())
        quantity.sort(reverse = True)
        def help(X, j):
            if j == len(quantity): return True
            for i, y in enumerate(X):
                if y >= quantity[j] and help(X[:i] + [y - quantity[j]] + X[i + 1:], j + 1): return True
            return False
        return help(X, 0)
