class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        def backtrack(i, curr_time):
            nonlocal ans
            if curr_time >= ans:
                return ans
            if i == len(jobs):
                ans = min(curr_time, ans)
                return
            for j in range(k):
                if j > 0 and t[j] == t[j - 1]:
                    continue
                t[j] += jobs[i]
                backtrack(i + 1, max(curr_time, t[j]))
                t[j] -= jobs[i]
        t = [0] * k
        ans = float('inf')
        backtrack(0, 0)
        return ans
