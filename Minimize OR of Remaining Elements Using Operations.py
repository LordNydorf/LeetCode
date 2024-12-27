class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for bit in range(31, -1, -1):
            cnt = 0
            cur = (1 << 31) - 1
            availability = res | (1 << bit) - 1
            for num in nums:
                cur = cur & num
                if cur | availability == availability:
                    cnt += 1
                    cur = (1 << 31) - 1
            if n - cnt > k:
                res += (1 << bit)
        return res
