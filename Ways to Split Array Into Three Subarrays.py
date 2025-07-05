class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = list(accumulate(nums))
        ans = 0
        n = len(nums)
        for i in range(n):
            j = bisect_left(prefix, 2 * prefix[i], lo = i + 1)
            k = bisect_right(prefix, (prefix[i] + prefix[-1]) // 2, hi = n - 1)
            if j >= k: 
                continue
            ans += k - j
        return ans % int(1e9 + 7)
