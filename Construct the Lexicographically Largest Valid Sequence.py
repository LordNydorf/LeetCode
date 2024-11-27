class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [0]*(2*n-1)
        i = 0                
        vi = [False] * (n+1)
        def dfs(arr, i, vi):
            if i >= (2*n-1):
                return True
            for x in range(n, 0, -1):
                if (x > 1 and ((not (arr[i] == 0 and (i+x < 2*n-1) and arr[i+x] == 0)) or vi[x]))  \
					or (x == 1 and (arr[i] != 0 or vi[x])):
                    continue
                if x > 1:
                    arr[i] = x
                    arr[i+x] = x
                else:
                    arr[i] = x
                vi[x] = True
                nexti = i+1
                while nexti < 2*n-1 and arr[nexti]:
                    nexti += 1				
                if dfs(arr, nexti, vi):
                    return True
                if x > 1:
                    arr[i] = 0
                    arr[i+x] = 0
                else:
                    arr[i] = 0
                vi[x] = False
            return False		
        dfs(arr, i, vi)
        return arr
