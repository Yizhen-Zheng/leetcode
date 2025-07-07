class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        self.size = 0

    def push(self, val: int) -> None:
        self.stack.append(val)

        if (not self.minimum) or self.minimum[-1] > val:
            self.minimum.append(val)
        else:
            self.minimum.append(self.minimum[-1])
        self.size += 1

    def pop(self) -> None:
        if self.size == 0:
            return None
        val = self.stack.pop()
        self.minimum.pop()
        return val

    def top(self) -> int:
        if self.size == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if self.size == 0:
            return None
        return self.minimum[-1]
        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(val)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()
