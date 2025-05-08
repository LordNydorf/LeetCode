class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        last_pos = {}
        res = [0 for i in range(n)]
        k_cnt = [0 for i in range(n+1)]
        for i, ele in enumerate(nums):
            k_cnt[i+1] = k_cnt[i] + int(ele == k)
            res[i] = 1 + k_cnt[i]
            if ele in last_pos:
                res[i] = max(res[i], res[last_pos[ele]] + 1)
            last_pos[ele] = i
        for i in range(n):
            res[i] += (k_cnt[-1] - k_cnt[i+1])
        return max(res)
