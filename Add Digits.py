class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num=str(num)
            num=[int(i) for i in num]    
            num=sum(num)
        return num
