class Solution:
    def findNumbers(self, nums):
        count = 0
        for x in nums:
            if self.isEven(x):
                count += 1
        return count
    def isEven(self, num):
        num_digits = self.nod(num)
        return num_digits % 2 == 0
    def nod(self, num):
        if num < 0:
            num *= -1
        return int(math.log10(num)) + 1
