class Solution:
    def minInsertions(self, s: str) -> int:        
        s = s.replace('))', '}')
        missing_brackets = 0
        required_closed = 0
        for c in s:
            if c == '(':
                required_closed += 2
            else:
                if c == ')': 
                    missing_brackets += 1
                if required_closed:
                    required_closed -= 2
                else:
                    missing_brackets += 1
        return missing_brackets + required_closed
