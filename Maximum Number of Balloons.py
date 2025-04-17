class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = {"b" : 0, "a" : 0, "l" : 0, "o" : 0, "n" : 0} 
        for c in text:
            if c in counter:
                counter[c] += 1
        double_c = min(counter['l'], counter['o']) // 2
        if min(counter.values()) < double_c:
            return min(counter.values())
        else:
            return double_c
