class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = 0
        for i in digits:
            integer = integer*10 + i
        integer += 1
        res = []
        while integer != 0:
            res.insert(0, integer % 10)
            integer = integer//10
        return res
