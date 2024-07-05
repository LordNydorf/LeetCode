class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = set()
        self.candidates = candidates
        self.targetSum = target
        for i, num in enumerate(candidates):
            self.backtrack([num], i, num)
        return self.res
    def backtrack(self, path, i, currentSum):
        if (currentSum >= self.targetSum):
            if currentSum == self.targetSum:
                pathTup = tuple(path)
                if pathTup not in self.res:
                    self.res.add(pathTup)
            return
        for j in range(i, len(self.candidates)):
            num = self.candidates[j]
            path.append(num)
            self.backtrack(path, j, currentSum + num)
            path.pop()
