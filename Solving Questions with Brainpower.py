class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(i: int) -> int:
            return 0 if i >= len(questions) else max(dfs(i + 1), questions[i][0] + dfs(i + 1 + questions[i][1]))
        return dfs(0)
