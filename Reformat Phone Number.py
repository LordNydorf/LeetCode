class Solution:
    def reformatNumber(self, number: str) -> str:
        new_num = ""
        for char in number:
            if char !='-' and char !=' ':
                new_num += char
        n = len(new_num)
        end = ""
        if n%3 == 1:
            end = new_num[-4:-2] + "-" + new_num[-2:]
            n -= 4
        elif n % 3 == 2:
            end = new_num[-2:]
            n -= 2
        res = ""
        i = 0
        while i < n:
            res += new_num[i]
            res += new_num[i+1]
            res += new_num[i+2]
            res += '-'
            i += 3
        if end == "":
            return res[:-1]
        return res + end
