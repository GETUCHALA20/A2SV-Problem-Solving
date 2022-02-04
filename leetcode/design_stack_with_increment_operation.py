class CustomStack:

    def __init__(self, maxSize: int):
        self.items = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.items) < self.maxSize:
            self.items.append(x)

    def pop(self) -> int:
        if len(self.items) > 0:
            return self.items.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        i= 0
        while i < k and i < len(self.items):
            self.items[i]+=val
            i+=1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)