class Solution:
    def minimizedStringLength(self, s: str) -> int:
        res = []
        for i in s:
            res.append(i)
        news = set(res)
        return len(news)
