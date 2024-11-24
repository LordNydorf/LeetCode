class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        n = len(nums)
        mod_seen = defaultdict(int)
        mod_seen[0] = 1
        for i in range(n):
            prefix = (prefix + nums[i]) % k
            mod_seen[prefix] += 1
            res += (mod_seen[prefix] - 1)
        return res
