class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        min_word_length = min(map(len, words))
        @cache
        def is_concatenated(word: str) -> bool:
            for i in range(min_word_length, len(word) - min_word_length + 1):
                if word[:i] in word_set and (word[i:] in word_set or is_concatenated(word[i:])):
                    return True
            return False
        return [word for word in words if is_concatenated(word)]
