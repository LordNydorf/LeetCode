class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        graph = {}
        i, j = 0, 0
        for c in ascii_uppercase:
            graph[c] = (i, j)
            j = (j + 1) % 6
            if j == 0:
                i += 1
        @cache
        def dp(idx, fi, fj, si, sj):
            if idx == n:
                return 0
            ii, jj = graph[word[idx]]
            ans = dp(idx + 1, ii, jj, si, sj) + (0 if fi == -1 and fj == -1 else abs(ii - fi) + abs(jj - fj))
            ans = min(ans, dp(idx + 1, fi, fj, ii, jj) + (0 if si ==- 1 and sj == -1 else abs(ii - si) + abs(jj - sj)))
            return ans
        return dp(0, -1, -1, -1, -1)
