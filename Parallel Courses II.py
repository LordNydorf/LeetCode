class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        children, total_time, visited, result = [[] for i in range(n)], [0] * n, set(range(n)), 0
        for u, v in relations:
            children[u - 1].append(v - 1)
            visited.discard(v - 1)
        stack = list(visited)
        while stack:
            tmp = stack[-1]
            total_time[tmp] = time[tmp]
            for child in children[tmp]:
                if total_time[child] <= 0: stack.append(child)
                else: total_time[tmp] = max(total_time[tmp], time[tmp] + total_time[child])
            if tmp == stack[-1]: 
                result = max(result, total_time[tmp])
                stack.pop(-1)
        return result       
