class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.limit = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) + 1 <= self.limit:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k >= len(self.stack):
            self.stack = [value + val for value in self.stack]
        else:
            self.stack = [value + val for value in self.stack[:k]] + self.stack[k:]


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)