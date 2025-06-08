class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(k) -> bool:
            remove_set = set(removable[:k])
            pointer = 0
            for i in range(len(s)):
                if i in remove_set:
                    continue
                if s[i] == p[pointer]:
                    pointer += 1
                    if pointer == len(p):
                        return True
            return False
        res = 0
        left, right = 1, len(removable)
        while left <= right:
            mid = (left + right) // 2
            if is_subsequence(mid):
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid - 1
        return res
