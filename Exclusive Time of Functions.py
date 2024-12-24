class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        d = [0] * n
        last_timestamp = 0
        for log in logs:
            ID, action, timestamp = log.split(':')
            ID, timestamp = int(ID), int(timestamp)
            if action == 'start':
                if stack:
                    d[stack[-1]] +=timestamp - last_timestamp
                stack.append(ID)
            elif action == 'end':
                d[stack.pop()] += timestamp - last_timestamp + 1
            last_timestamp = timestamp + int(action == 'end')
        return d
