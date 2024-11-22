class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split(" ")
        sentence2 = sentence2.split(" ")
        if sentence1 == sentence2: return True
        prefix, suffix = [], []
        n, m = len(sentence1), len(sentence2)
        for i in range(min(n, m)):
            if sentence1[i] == sentence2[i]:
                prefix.append(sentence1[i])
            else:
                break        
        for i in range(min(len(sentence1), len(sentence2))):
            if sentence1[n - i - 1] == sentence2[m - i - 1]:
                suffix.append(sentence1[n - i - 1])
            else:
                break
        suffix.reverse()        
        while len(suffix) + len(prefix) > min(n, m):
            if suffix[0] == prefix[-1]:
                prefix.pop()
        prefix.extend(suffix)
        return prefix == sentence1 or prefix == sentence2
