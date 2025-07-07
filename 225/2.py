from collections import deque


class MyStack:
    '''
    get last in data use 1 queues
    '''

    def __init__(self):
        # only be able to get [0] of queue
        self.queue = deque()
        self.last = None
        self.size = 0

    def push(self, x: int) -> None:
        # update peek
        self.queue.append(x)
        for _ in range(self.size):
            val = self.queue.popleft()
            self.queue.append(val)

        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return None
        val = self.queue.popleft()
        self.size -= 1
        return val

    def top(self) -> int:
        if self.empty():
            return None
        self.last = self.queue[0]
        return self.last

    def empty(self) -> bool:
        return self.size == 0
        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()
