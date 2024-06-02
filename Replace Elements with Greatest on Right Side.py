class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightValue = -1
        for i in range(len(arr)-1, -1, -1):
            maxValue = max(rightValue, arr[i])
            arr[i] = rightValue
            rightValue = maxValue
        return arr
