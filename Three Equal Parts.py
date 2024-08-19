class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = [i for i, j in enumerate(arr) if j == 1]
        n=len(ones)
        if not ones:
            return [0, 2]
        if n % 3:
            return [-1, -1]
        i,j,k = ones[0], ones[n // 3], ones[n // 3 * 2]
        l = len(arr) - k
        if arr[i:i+l] == arr[j : j + l] == arr[k : k + l]:
            return [i + l - 1, j + l]
        return [-1, -1]
