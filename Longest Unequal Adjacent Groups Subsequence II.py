class Solution:
    def getWordsInLongestSubsequence(self, n, words, groups):
        dp = [1] * len(groups)
        pv = [-1] * len(groups)
        for i in range(1, len(groups)):
            for j in range(i):
                if groups[i] == groups[j]:
                    continue
                if len(words[i]) != len(words[j]):
                    continue
                diff = sum(1 for k in range(len(words[i])) if words[i][k] != words[j][k])
                if diff != 1:
                    continue
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pv[i] = j
        wi = dp.index(max(dp))
        ans = []
        while wi != -1:
            ans.append(words[wi])
            wi = pv[wi]
        ans.reverse()
        return ans
