class Solution:
    def minCosts(self, cost: list[int]) -> list[int]:
        answer = []
        curr = float('inf')
        for x in cost:
            curr = min(curr, x)
            answer.append(curr)
        return answer
