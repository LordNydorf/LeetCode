class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        temp = 0
        res = 0
        for i in range(len(arr1)):
            temp = 0
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])>d:
                    temp += 1
                    if j == len(arr2) - 1 and temp == len(arr2):
                        res += 1
        return res
