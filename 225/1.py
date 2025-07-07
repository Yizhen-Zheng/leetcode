from collections import deque


class MyStack:
    '''
    get last in data use 2 queues
    '''

    def __init__(self):
        # only be able to get [0] of queue
        self.queue_a = deque()
        self.queue_b = deque()
        self.last = None
        self.size = 0

    def push(self, x: int) -> None:
        # update peek
        self.last = x
        self.queue_a.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return None
        while len(self.queue_a) > 1:
            val = self.queue_a.popleft()
            self.queue_b.append(val)
        val = self.queue_a.popleft()
        self.size -= 1
        self.queue_a = self.queue_b
        self.queue_b = deque()
        return val

    def top(self) -> int:

        return self.last

    def empty(self) -> bool:
        return self.size == 0
        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()
