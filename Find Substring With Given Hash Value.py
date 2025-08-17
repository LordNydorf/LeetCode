class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        val = lambda v: ord(v) - ord("a") + 1
        powers = [pow(power, i, modulo) for i in range(k)]
        idx = n - k
        hash_val = 0
        for i in range(k):
            hash_val += val(s[n - k + i]) * powers[i]
        for i in range(n - k - 1, -1, -1):
            hash_val = ((hash_val - val(s[i + k]) * powers[k - 1]) * power + val(s[i])) % modulo
            if hash_val == hashValue:
                idx = i
        return s[idx : idx + k]
