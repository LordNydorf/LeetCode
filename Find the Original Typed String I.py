class Solution:
    def possibleStringCount(self, word: str) -> int:
        return sum(len(list(x)) - 1 for _, x in groupby(word)) + 1
