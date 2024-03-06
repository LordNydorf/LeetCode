class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        palindrome = 0
        while temp != 0:
            palindrome = (palindrome * 10) + (temp % 10)
            temp = temp // 10
        if palindrome == x:
            return True
