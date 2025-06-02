class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ''
        for i in range(len(s)): 
            cnt = 0 
            for j in range(i, len(s)): 
                if s[j] == '1': cnt += 1
                if cnt == k: 
                    if ans == '' or len(ans) > j-i+1: ans = s[i:j+1]
                    elif len(ans) == j-i+1: ans = min(ans, s[i:j+1])
                    break 
        return ans 
