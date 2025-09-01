class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        size = 5
        curx, cury = 0, 0
        offset = ord('a')
        ans = '' 
        for i in target:
            row = (ord(i)-offset)//size
            col = (ord(i)-offset)%size
            if curx > col: ans += 'L'*(curx-col)
            if row > cury: ans += 'D'*(row-cury)
            if cury > row: ans += 'U'*(cury-row)    
            if col > curx: ans += 'R'*(col-curx)
            ans += '!'
            curx, cury = col, row
        return ans
