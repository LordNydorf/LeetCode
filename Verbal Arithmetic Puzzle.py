class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        words.append(result)
        rows, cols = len(words), max(map(len, words))
        LTD = {}
        DTL = [None] * 10
        def search(row, col,  bal):
            if col >= cols:
                return bal == 0
            if row >= rows:
                return bal % 10 == 0 and search(0, col + 1, bal // 10)
            word = words[row]
            if col >= len(word):
                return search(row + 1, col, bal)
            letter = word[len(word) - 1 - col]
            sign = 1 if row < rows - 1 else -1
            if letter in LTD and (LTD[letter] or len(word) == 1 or col != len(word) - 1):
                return search(row + 1, col, bal + (sign * LTD[letter]))
            else:
                for d,c in enumerate(DTL):
                    if not c and (d or len(word) == 1 or col != len(word) - 1):
                        LTD[letter] = d
                        DTL[d] = letter
                        if search(row + 1, col, bal + (sign * LTD[letter])):
                            return True
                        else:
                            DTL[d] = None
                            if letter in LTD:
                                del LTD[letter]
            return False
        return search(0, 0, 0)
