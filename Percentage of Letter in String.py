class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            if s[i] == letter:
                count += 100
        perc = count//n
        return perc
