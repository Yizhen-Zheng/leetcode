from collections import defaultdict, OrderedDict

'''
10min+20min+debug20min

'''


class LRUCache:
    class ListNode:
        def __init__(self, val, key, prev=None, next=None):
            self.val = val
            self.key = key
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.head = self.ListNode('dummy', None)
        self.tail = self.ListNode('dummy', None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.table = defaultdict(lambda: None)
        self.capacity = capacity
        self.item_conut = 0
        return

    def get(self, key: int) -> int:
        node = self.table.get(key)
        print(node)
        print('get')
        if not node:
            return -1
        # move node to head
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.head
        node.next = self.head.next
        origin_head = self.head.next
        origin_head.prev = node
        self.head.next = node
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.table.get(key)
        print()
        print(node)
        print(self.item_conut)
        print()

        if not node:  # put new val
            node = self.ListNode(value, key, self.head, self.head.next)
            if self.item_conut == self.capacity:  # need to remove existing
                remove = self.tail.prev  # get tail node
                # remove from LL
                self.tail.prev = remove.prev
                remove.prev.next = self.tail
                # remove from hashtable
                self.table[remove.key] = None
            else:
                self.item_conut += 1
            # add new node to hashtable
            self.table[key] = node
        else:  # update eixsting
            # reconnect parts
            node.prev.next = node.next
            node.next.prev = node.prev
            node.val = value
            node.prev = self.head
            node.next = self.head.next
        # add node to head
        origin_head = self.head.next
        origin_head.prev = node
        self.head.next = node
        return

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)


class LRUCache:
    '''use orderedDict'''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buket = OrderedDict()

    def get(self, key: int) -> int:
        val = self.buket.get(key)
        if val == None:
            return -1
        self.buket.move_to_end(key)  # activate key
        return val

    def put(self, key: int, value: int) -> None:
        val = self.buket.get(key)
        if not val:  # need to add new, check size
            if len(self.buket) >= self.capacity:
                self.buket.popitem(False)  # remove tail in FIFO
        else:  # last activate
            self.buket.move_to_end(key)  # move active to end(last accessed)
        self.buket[key] = value


class LRUCache:
    '''use plain dict'''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buket = {}

    def get(self, key: int) -> int:
        val = self.buket.get(key)
        if val == None:
            return -1
        del self.buket[key]
        self.buket[key] = val  # activate key
        return val

    def put(self, key: int, value: int) -> None:
        val = self.buket.get(key)
        if not val:  # need to add new, check size
            if len(self.buket) >= self.capacity:
                first_in = next(iter(self.buket))
                self.buket.pop(first_in)  # remove tail in FIFO
        else:  # last activate
            self.buket.pop(key)  # move active to end(last accessed)
        self.buket[key] = value


r = LRUCache(2)
r.put(1, 0)
r.put(2, 2)
n = r.get(1)
print(n)
r.put(3, 3)
n = r.get(2)
print(n)
