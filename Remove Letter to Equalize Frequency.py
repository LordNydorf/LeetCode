class Solution:
    def equalFrequency(self, word: str) -> bool:
        def all_equal(lst):
            return not lst or [lst[0]] * len(lst) == lst
        hash = {}
        for letter in word:
            hash.setdefault(letter, 0)
            hash[letter] += 1
        vals = list(hash.values())
        for i in range(len(vals)):
            vals = list(hash.values())
            vals[i] -= 1
            if vals[i] == 0:
                vals.pop(i)
            if all_equal(vals):
                return True
        return False
