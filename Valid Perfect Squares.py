class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        integer = num ** 0.5
        if int(integer) * int(integer) == num:
            return True
        else:
            return False
