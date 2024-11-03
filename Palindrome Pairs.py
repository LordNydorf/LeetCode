class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words_map = {word : i for i, word in enumerate(words)}
        answers = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                prefix, suffix = word[:j], word[j:]
                if prefix == prefix[::-1]:
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in words_map and i != words_map[reversed_suffix]:
                        answers.append([words_map[reversed_suffix],i])                
                if j != len(word) and suffix == suffix[::-1]:
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in words_map and i != words_map[reversed_prefix]:
                        answers.append([i,words_map[reversed_prefix]])
        return answers    
