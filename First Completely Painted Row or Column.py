class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        i = 0
        m = len(mat)
        n = len(mat[0])
        mark_r = [0 for i in range(m)]
        mark_c =  [0 for i in range(n)]
        mapping = {}
        for j in range (m*n):
            mapping.update({mat[j//n][j%n]: [j//n,j%n]})
        while i in range(m*n):
            mark_r[mapping[arr[i]][0]] += 1
            if mark_r[mapping[arr[i]][0]] ==n:
                return i
            mark_c[mapping[arr[i]][1]] += 1
            if mark_c[mapping[arr[i]][1]] == m:
                return i
            i += 1
