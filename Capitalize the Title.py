class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title.lower()
        ts = title.split(" ")
        res = ""
        for s in ts :
            if len(s) <= 2 :
                res += s.lower() + " "
                continue
            res += s.capitalize() + " "
        return res[:-1]
