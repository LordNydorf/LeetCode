class Solution:
    def isValid(self, s: str) -> bool:
        l1 = []
        compare = ""
        flag = 0
        for i in s:
            if i in "({[":
                l1.append(i)
            elif i in ")}]":
                if not l1:
                    flag = 0
                    break
                else:
                    compare = l1.pop(-1)
                    compare = compare + i
                    if compare == '()' or compare == '{}' or compare == '[]':
                        flag = 1
                    else:
                        flag = 0
                        break
        if flag == 0 or len(l1) != 0:
            return False
        else:
            return True
        
