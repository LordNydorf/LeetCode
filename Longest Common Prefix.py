class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        if size == 1:
            return strs[0]
        strs.sort()
        mlen = min(len(strs[0]), len(strs[-1]))
        i = 0
        while (i < mlen and strs[0][i] == strs[-1][i]):
            i += 1
        prefix = strs[0][0:i]
        return prefix
