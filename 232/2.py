class MyQueue:
    '''
    O(1), every in into in_stack, then when pop, it goes into out_stack, and never back to in
    '''

    def __init__(self):
        self.stack_a = []
        self.stack_b = []
        self.first = None
        self.size = 0

    def push(self, x: int) -> None:
        if self.empty():
            self.first = x  # update peek
        self.size += 1
        self.stack_a.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        self.peek()
        if not self.stack_b:
            return None
        val = self.stack_b.pop()
        self.size -= 1
        return val

    def peek(self) -> int:
        if not self.stack_b:  # dump in into out
            while self.stack_a:
                val = self.stack_a.pop()
                self.stack_b.append(val)
        # set peek
        if self.stack_b:
            self.first = self.stack_b[-1]
        else:
            self.first = None

        return self.first

    def empty(self) -> bool:
        return self.size == 0
        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()
