class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        left = 0
        right = 1
        res = []
        while left < len(prices) - 1 and right < len(prices):
            if prices[right] <= prices[left]:
                res.append(prices[left] - prices[right])
                left += 1
                right = left + 1
            else:
                right += 1
                if right == len(prices):
                    res.append(prices[left])
                    left += 1
                    right = left + 1
        return res + [prices[-1]]
