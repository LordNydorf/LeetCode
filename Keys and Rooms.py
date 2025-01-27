class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = []
        for i in rooms[0]:
            stack.append(i)
        v = [0] * len(rooms)
        v[0] = 1
        while(stack):
            i = stack.pop()
            if(v[i] == 0):
                v[i] = 1
                for j in rooms[i]:
                    stack.append(j)
        return not (0 in v)
