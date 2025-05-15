class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        s = set()
        for x in range(len(number)):
            if number[x] == digit:
                s.add(number[0 : x] + number[x + 1 : ])
                continue
        return max(s)
