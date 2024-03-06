class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        str1, str2 = Counter(ransomNote), Counter(magazine)
        return str1 & str2 == str1
