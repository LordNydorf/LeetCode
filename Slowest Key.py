class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releasesTimes = []
        maxTime = releaseTimes[0]
        releasesTimes.append(maxTime)
        maxPressed = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            releasesTimes.append(releaseTimes[i] - releaseTimes[i-1])
            if releasesTimes[i] > maxTime:
                maxTime = releasesTimes[i]
                maxPressed = keysPressed[i]
            elif releasesTimes[i] == maxTime:
                if keysPressed[i] > maxPressed:
                    maxPressed = keysPressed[i]
        return maxPressed
