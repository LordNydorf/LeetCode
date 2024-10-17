class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        l,w,nl,ans = 0,defaultdict(int),len(logs),[0]*(m:= len(queries))
        logs.extend((0,t,e) for e,t in enumerate(queries ))
        logs.sort( key=lambda x:x[1] )
        for r in range(nl+m):
            a=logs[r][1] - x
            for l in range(l,r):
                if logs[l][1]>=a:break
                w[v:=logs[l][0]] -= 1
                if not w[v]:  w.pop(v)
                l += 1
            w[v:=logs[r][0]]+=1
            if not v: ans[logs[r][2]] = n - len(w) + 1
        return ans
