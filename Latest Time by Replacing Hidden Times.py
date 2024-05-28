class Solution:
    def maximumTime(self, time: str) -> str:
        print(len(time))
        if time[0:2] == "??":
            time = "23" + time[2:]
        if time[0] == "?" and time[1] < "4":
            time = "2" + time[1:] 
        if time[0] == "?" and time[1] >= "4":
            time = "1" + time[1:]
        if time[1] == "?":
            if time[0] == "0" or time[0] == "1":
                time = time[0] + "9" + time[2:]
            else:
                time = time[0] + "3" + time[2:]
        if time[3] == "?":
            time = time[0:3] + "5" + time[4]
        if time[4] == "?":
            time = time[0:4] + "9"
        return time
