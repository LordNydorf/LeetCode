class Solution:
    def splitNum(self, num: int) -> int:
        num1=''
        num2=''
        x = [int(i) for i in str(num)]
        x.sort()
        print(x)
        for i in range(len(x)):
            if i%2 == 0:
                num1 = num1 + str(x[i])
            else:
                num2 = num2 + str(x[i])
        return int(num1) + int(num2)
