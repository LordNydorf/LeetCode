class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def generat_results(a, b):
            res = [a + b, a - b, b - a, a * b]
            if a:
                res.append(b / a)
            if b:
                res.append(a / b)
            return res


        def check(cards):
            if len(cards) == 1:
                return abs(cards[0] - 24.0) <= 0.1
            for i in range(len(cards)):
                for j in range(i + 1, len(cards)):
                    new_list = [num for k, num in enumerate(cards) if (k != i and k != j)]
                    for res in generat_results(cards[i], cards[j]):
                        new_list.append(res)
                        if check(new_list):
                            return True
                        new_list.pop()
            return False
        return check(cards)
