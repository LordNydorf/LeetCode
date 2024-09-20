class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_taken = []
        for i in range(len(position)):
            time_taken.append((target-position[i])/speed[i])
        combined = list(zip(position, speed, time_taken))
        combined_sorted = sorted(combined, key = lambda x: x[0],reverse = True)
        car_fleet = 0
        stk = []
        for i in combined_sorted:
            if not stk or stk[0] - i[2] >= 0:
                stk.append(i[2])
            else:
                car_fleet += 1
                stk = [i[2]]
        if len(stk) > 0:
            car_fleet += 1
        return car_fleet
