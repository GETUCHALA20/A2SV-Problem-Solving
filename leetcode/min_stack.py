class MinStack:

    def __init__(self):
        self.items = []
        self.minIndex = 0

    def push(self, val: int) -> None:
        if self.items:
            if val < self.items[self.minIndex]:
                self.minIndex = len(self.items)
            self.items.append(val)
        else:
            self.minIndex = 0
            self.items.append(val)
        

    def pop(self) -> None:
        self.items.pop()
        if self.minIndex == len(self.items):
            self.minIndex = len(self.items)-1
            for i in range(len(self.items)-1):
                if self.items[i] < self.items[self.minIndex]:
                    self.minIndex = i
    def top(self) -> int:
        return self.items[len(self.items)-1]

    def getMin(self) -> int:
        return self.items[self.minIndex]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()