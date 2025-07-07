class MyQueue:
    '''
    close to O(1),cuz push potentially dump out back to in
    '''

    def __init__(self):
        self.stack_a = []
        self.stack_b = []
        self.first = None
        self.current_is_a = True  # if currently all elements are in a
        self.size = 0

    def push(self, x: int) -> None:
        if self.empty():
            self.first = x  # update peek
        if not self.current_is_a:
            self.current_is_a = True
            while self.stack_b:
                val = self.stack_b.pop()
                self.stack_a.append(val)
        self.size += 1
        self.stack_a.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.current_is_a:  # need to pop all
            self.current_is_a = False
            while self.stack_a:
                val = self.stack_a.pop()
                self.stack_b.append(val)
        self.size -= 1
        val = self.stack_b.pop()
        if self.stack_b:
            self.first = self.stack_b[-1]  # update peek
        return val

    def peek(self) -> int:
        return self.first

    def empty(self) -> bool:
        return self.size == 0
        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()
