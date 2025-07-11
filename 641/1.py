class LinkedListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


class MyCircularDeque:
    '''

    ptr to head 
    ptr to tail
    size
    how to 
    head no prev, tail no next -> head prev = tail tail next = head
    '''

    def __init__(self, k: int):
        self.limit = k
        self.size = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        '''tail not change, only change head'''
        if self.isFull():
            return False
        new_node = LinkedListNode(value, None, None)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = LinkedListNode(value, None, None)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            node_to_remove = self.head
            self.head = node_to_remove.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            node_to_remove = self.tail
            self.tail = node_to_remove.prev
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

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
