class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        return reduce(lambda p,r:(p[0]+p[1]*c,c) if (c:=r.count('1')) else p, bank, (0,0))[0]
