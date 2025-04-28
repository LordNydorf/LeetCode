class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        if max(Counter(nums).values()) > k: return -1
        if k == n: return 0
        if k == 1: return nums[n - 1] - nums[0]
        next_larger, cur, next_ptr = [0 for _ in range(n)], nums[-1], n
        for i in range(n - 1, -1, -1):
            if nums[i] != cur: cur, next_ptr = nums[i], i + 1
            next_larger[i] = next_ptr
        len_set = n // k - 1
        @cache
        def dp(i: int, mask: int, size: int) -> int:
            if mask == (1 << n) - 1: return 0
            if i == n: return float("inf")
            if mask & (1 << i): return dp(i + 1, mask, size)
            new_i, new_mask, new_size = next_larger[i], mask | (1 << i), size + 1
            if size == 0: return dp(new_i, new_mask, new_size) - nums[i]
            elif size < len_set: return min(
                dp(new_i, new_mask, new_size),
                dp(new_i, mask, size)
            )
            else: return min(
                dp(0, new_mask, 0) + nums[i], dp(new_i, mask, size)
            )
        return dp(0, 0, 0)
