class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:           
        sorted_heights = sorted(zip(heights, names), reverse=True)
        res = [n for h, n in sorted_heights]
        return res       
