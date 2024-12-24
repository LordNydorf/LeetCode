class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        endLink = None
        cnt = 0
        pairs.sort(key = lambda x :x[1])
        for start, end in pairs:
            if endLink == None:
                cnt += 1
                endLink = end
            else:
                if endLink < start:
                    cnt += 1
                    endLink = end
        return cnt
