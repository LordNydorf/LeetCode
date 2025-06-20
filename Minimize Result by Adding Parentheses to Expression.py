class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus = expression.index("+")
        self.min_expr = float('inf')
        self.min_output = ""
        def dfs(left, right):
            if left < 0 or right >= len(expression):
                return
            left_add = int(expression[left:plus])
            right_add = int(expression[plus + 1: right + 1])
            add = left_add + right_add
            left_mult = int(expression[0:left]) if left != 0 else 1
            right_mult = int(expression[right + 1:]) if right + 1 < len(expression) else 1
            if(left_mult * add * right_mult < self.min_expr):
                self.min_output = expression[0:left] + "(" + expression[left:plus] + "+" + expression[plus + 1: right + 1] + ")" + expression[right + 1:]
                self.min_expr = left_mult * add * right_mult
            dfs(left - 1, right)
            dfs(left, right + 1)
        dfs(plus - 1, plus + 1)
        return self.min_output
