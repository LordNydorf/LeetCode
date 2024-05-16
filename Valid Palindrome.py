class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(char for char in s if char.isalnum())
        ss = clean_s.lower()
        t = ss[::-1]
        if t == ss:
            return True
        else:
            return False
