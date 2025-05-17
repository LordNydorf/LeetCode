class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(set)
        balls = {}  
        answer = []
        for ball, color in queries:
            if ball in balls:
                prev_color = balls[ball]
                colors[prev_color].remove(ball)
                if not colors[prev_color]:
                    del colors[prev_color]
            balls[ball] = color
            colors[color].add(ball)
            answer.append(len(colors))
        return answer
