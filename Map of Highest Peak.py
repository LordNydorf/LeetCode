class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        maps = []
        for a in range(len(isWater)):
            temp = []
            for b in range(len(isWater[0])):
                temp.append(isWater[a][b])
                if isWater[a][b] == 0:
                    isWater[a][b] = 'L'
                else:
                    isWater[a][b] = 'W'
            maps.append(temp)
        dire = [[-1,0],[0,1],[1,0],[0,-1]]
        edge = []
        print(isWater)
        for a in range(len(isWater)):
            for b in range(len(isWater[0])):
                if isWater[a][b] == 'W':
                    maps[a][b] = 0                    
                    for q in dire:
                        if 0 <= a + q[0] < len(isWater) and 0 <= b + q[1] <len(isWater[0]):
                            if isWater[a + q[0]][b + q[1]] == 'L':
                                maps[a + q[0]][b + q[1]] = 1
                                edge.append([a + q[0], b + q[1]])
                else:
                    if maps[a][b] != 1:
                        maps[a][b] = None
        while len(edge) > 0:
            temp = []
            for a in edge:
                for q in dire:
                    if 0 <= a[0] + q[0] < len(isWater) and 0 <= a[1] + q[1] < len(isWater[0]):
                        if maps[a[0] + q[0]][a[1] + q[1]] == None:
                                maps[a[0] + q[0]][a[1] + q[1]] = maps[a[0]][a[1]] + 1
                                temp.append([a[0] + q[0], a[1] + q[1]])
            edge = temp.copy()
        return maps
