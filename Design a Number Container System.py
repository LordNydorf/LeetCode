from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.mp = {}
        self.data = defaultdict(SortedList)
        
    def change(self, index: int, number: int) -> None:
        if index in self.mp: 
            oldNumber = self.mp[index]
            self.data[oldNumber].remove(index)
        self.mp[index] = number 
        self.data[number].add(index)
        
    def find(self, number: int) -> int:
        if self.data[number]: return self.data[number][0]
        return -1
