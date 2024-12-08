class Solution:
    def countTriples(self, n: int) -> int:
        counter = 0
        square = set()
        for i in range(n + 1):
            square.add(i ** 2)
        for i in range(1, n):
            for j in range(i + 1, n):
                if((i ** 2 + j ** 2) in square): 
                    print(i ** 2 + j ** 2)
                    counter += 1
        return counter * 2
