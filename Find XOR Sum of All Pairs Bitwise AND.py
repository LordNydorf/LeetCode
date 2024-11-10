class Solution:
    def getXORSum(self, arr1, arr2):
        a, b = 0, 0
        for num in arr1:
            a ^= num
        for num in arr2:
            b ^= num
        return a & b
