class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        y = y // 4
        x = min(x, y)
        if x % 2 == 1:
            return "Alice"
        else:
            return "Bob"
