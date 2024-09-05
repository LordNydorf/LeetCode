class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck)        
        nums = list(freq.values())
        gcd = math.gcd(*nums)
        return gcd != 1
