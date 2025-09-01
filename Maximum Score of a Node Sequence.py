class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        def explore(sequence, depth, current_score):
            nonlocal max_score
            if depth == 4:
                max_score = max(max_score, current_score)
                return
            if current_score + (4 - depth) * ms <= max_score:
                return
            for neighbor in graph[sequence[-1]]:
                if neighbor not in sequence:                    
                    sequence.append(neighbor)
                    explore(sequence, depth+1, current_score + scores[neighbor])
                    sequence.pop()
        n = len(scores)
        max_score = -1
        ms = max(scores)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        sorted_nodes = sorted(range(n), key=lambda x: scores[x], reverse=True)           
        for idx in sorted_nodes:
            explore([idx], 1, scores[idx])
        return max_score 
