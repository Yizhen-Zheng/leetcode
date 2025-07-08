
class MyCircularDeque:
    '''

    ptr to head 
    ptr to tail
    size
    head no prev, tail no next -> head prev = tail tail next = head
    further optimization:
    only keep head and size, get tail idx everytime get tail / infert
    benifits: when delete tail, only reduce size, no need to move tail idx and check
    handle edge case naturally
    '''

    def __init__(self, k: int):
        self.limit = k
        self.size = 0
        self.head = 0
        self.tail = 0
        self.queue = [None]*k

    def insertFront(self, value: int) -> bool:
        '''tail not change, only change head'''
        if self.isFull():
            return False
        if self.size > 0:
            self.head = (self.head - 1)if (self.head > 0) else (self.limit - 1)
        self.queue[self.head] = value

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.size > 0:
            self.tail = self.tail+1 if self.tail < self.limit-1 else 0
        self.queue[self.tail] = value

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.size > 1:
            self.head = self.head+1 if self.head < self.limit-1 else 0

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.size > 1:
            self.tail = self.tail-1 if self.tail > 0 else self.limit-1

        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit
        # Your MyCircularDeque object will be instantiated and called as such:
        # obj = MyCircularDeque(k)
        # param_1 = obj.insertFront(value)
        # param_2 = obj.insertLast(value)
        # param_3 = obj.deleteFront()
        # param_4 = obj.deleteLast()
        # param_5 = obj.getFront()
        # param_6 = obj.getRear()
        # param_7 = obj.isEmpty()
        # param_8 = obj.isFull()
