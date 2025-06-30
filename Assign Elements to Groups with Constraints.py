class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        d, mx = defaultdict(lambda: -1), max(groups)+1
        for i, element in enumerate(elements):
            if element in d: continue
            for num in range(element, mx, element):
                if num in d: continue
                d[num] = i
        return list(map(lambda x: d[x], groups))
