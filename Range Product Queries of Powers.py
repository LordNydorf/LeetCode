class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        cur = bin(int(n))[2:]
        now = cur[::-1]
        mod = ((10 ** 9) + 7)
        print(now)
        key = []
        for i, n in enumerate(now):
            if n == "0":
                continue
            else:
                key.append(2 ** i)
        print(key)
        ans = []
        for q in queries:
            s, e = q[0], q[1]
            ans.append(math.prod(key[s: e + 1]) % mod)
        print(ans)
        return ans
