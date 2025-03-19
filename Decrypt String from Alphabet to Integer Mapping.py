class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0 
        l = []
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                n = int(s[i:i+2])
                l.append(chr(n + ord("a")-1))
                i += 3
            else :
                n = int(s[i])
                l.append(chr(n + ord("a")-1))
                i += 1
        return "".join(l)
