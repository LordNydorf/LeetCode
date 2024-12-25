import math
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if (x + y) < target:
            return False
        elif (x + y) == target or x == target or y == target:
            return True
        else:
            return(target % math.gcd(x, y) == 0)
