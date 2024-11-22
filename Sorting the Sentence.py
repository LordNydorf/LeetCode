class Solution:
    def sortSentence(self, s: str) -> str:
        arr = [(w[-1], w[:-1]) for w in s.split(" ")]
        arr.sort()
        return " ".join([w for _, w in arr])
