class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = float('-inf')
        for j in range(n - k - 1, -1, -1):
            energy[j] += energy[j + k]
        for i in range(n):
            ans = max(ans, energy[i])
        return ans
