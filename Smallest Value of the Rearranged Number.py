class Solution:
    def smallestNumber(self, num: int) -> int:
        digit_count = Counter(str(abs(num)))
        res = ""
        for i in range(1, 10):
            res += str(i) * digit_count[str(i)]
        if num > 0:
            res = res[0] + "0" * digit_count["0"] + res[1:]
        else:
            res = res[::-1]
            res = "-" + res + "0" * digit_count["0"]
        return int(res)
