class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return self.allCapitals(word) or self.allSmalls(word) or self.capitalized(word)
    def allCapitals(self,word:str):
        return word == word.upper()
    def allSmalls(self,word:str):
        return word == word.lower()
    def capitalized(self,word:str):
        return word == word.capitalize()
