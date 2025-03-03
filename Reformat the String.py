class Solution:
    def reformat(self, s: str) -> str:
        letters = [i for i in s if i.isalpha()]
        digits = [i for i in s if i.isdigit()]
        l = len(letters)
        d = len(digits)
        ans = ""
        exist = [-1, 0, 1]
        if (l-d) not in exist:
            return ans
        elif l > d:
            for i in range(l):
                if i != l - 1:
                    ans += letters[i] + digits[i]
                else:
                    ans += letters[i]
        elif l == d:
            for i in range(l):
                ans += letters[i] + digits[i]
        else:
            for i in range(d):
                if i != d - 1:
                    ans += digits[i] + letters[i]
                else:
                    ans += digits[i]
        return ans
