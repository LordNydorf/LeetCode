class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for elem in arr2:
            while elem > 0:
                prefixes.add(elem)
                elem //= 10
        result = 0
        for elem in arr1:
            while elem > result:
                if elem in prefixes:
                    result = max(result, elem)
                    break
                else:
                    elem //= 10 
        if result == 0:
            return 0
        return len(str(result))
