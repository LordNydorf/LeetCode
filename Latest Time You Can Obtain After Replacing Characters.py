class Solution:
    def findLatestTime(self, s: str) -> str:
        hr0, hr1, _ , mn0, mn1 = list(s)
        if hr0 == '?': hr0 = '1' if hr1 in '?01' else '0'
        if hr1 == '?': hr1 = '9' if hr0 == '0' else '1'
        if mn0 == '?': mn0 = '5'
        if mn1 == '?': mn1 = '9'    
        return hr0 + hr1 + ':' + mn0 + mn1
