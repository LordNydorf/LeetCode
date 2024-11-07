class Solution:
    def maximumHappinessSum(self, a: List[int], k: int) -> int:
        return sum(v-i for i,v in takewhile(lambda q:lt(*q),enumerate(nlargest(k,a))))
