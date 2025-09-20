from collections import defaultdict
from math import inf


class AllOne:
    '''
    20:50-21:17
    dec must exist
    get min and max may not exist
    watched solution
    '''

    def __init__(self):
        self.key_freq = defaultdict(int)  # remove after elem count become 0
        self.freq_key = defaultdict(set)
        self.max_c = 0
        self.min_c = 0

        return

    def inc(self, key: str) -> None:
        if len(self.key_freq) == 0:
            self.min_c = 1  # if first elem added in, it's also the min item
        origin_count = self.key_freq[key]

        self.key_freq[key] = origin_count+1  # increase count of that key
        # if origin is 0, means haven't presented yet
        if origin_count > 0:  # the key previously exists
            prev_set = self.freq_key[origin_count]  # remove from that count group
            prev_set.remove(key)
        self.freq_key[origin_count+1].add(key)  # add to new count group

        if self.max_c < origin_count+1:  # update max_c
            self.max_c = origin_count+1

        return

    def dec(self, key: str) -> None:
        origin_count = self.key_freq[key]
        # remove from set
        self.freq_key[origin_count].remove(key)
        if origin_count-1 == 0:  # remove elem completely
            del self.key_freq[key]
            # no elem in whole DS
            if len(self.key_freq) == 0:
                self.min_c, self.max_c = 0, 0
        else:  # has atlease 1 remaining elem
            self.key_freq[key] = origin_count-1
            self.freq_key[origin_count-1].add(key)  # move to origin_count-1 set
            if self.min_c > origin_count-1:
                self.min_c = origin_count-1
            if len(self.freq_key[self.max_c]) == 0:
                self.max_c -= 1

        return

    def getMaxKey(self) -> str:
        if self.max_c == 0:
            return ''
        elem = list(self.freq_key[self.max_c])[0]

        return elem

    def getMinKey(self) -> str:
        if self.min_c == 0:
            return ''
        elem = list(self.freq_key[self.min_c])[0]

        return elem

        # Your AllOne object will be instantiated and called as such:
        # obj = AllOne()
        # obj.inc(key)
        # obj.dec(key)
        # param_3 = obj.getMaxKey()
        # param_4 = obj.getMinKey()

# ---------------------


'''
watched solution
'''


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val
        self.keys = set()


class AllOne:

    def __init__(self):
        self.key_to_bucket = {}  # key -> DL node
        self.zero_node = ListNode(0, None, None)
        self.inf_node = ListNode(float('inf'), None, None)
        self.zero_node.next = self.inf_node
        self.inf_node.prev = self.zero_node
        return

    def inc(self, key: str) -> None:
        origin_bucket = self.key_to_bucket.get(key, self.zero_node)
        if origin_bucket.next.val != origin_bucket.val+1:  # there's no node for the new count number, create one
            destination = ListNode(origin_bucket.val+1, origin_bucket, origin_bucket.next)
            destination.next.prev = destination  # reconnect
            destination.prev.next = destination
        else:  # the node we're going to add things in already exists
            destination = origin_bucket.next

        if origin_bucket is not self.zero_node:  # remove from previous if needed
            origin_bucket.keys.remove(key)
            if len(origin_bucket.keys) == 0:  # remove
                origin_bucket.prev.next = origin_bucket.next
                origin_bucket.next.prev = origin_bucket.prev
        destination.keys.add(key)
        self.key_to_bucket[key] = destination
        return

    def dec(self, key: str) -> None:
        origin_bucket = self.key_to_bucket.get(key, self.inf_node)
        if origin_bucket.prev.val != origin_bucket.val-1:  # there's no node for the new count number, create one
            destination = ListNode(origin_bucket.val-1, origin_bucket.prev, origin_bucket)
            destination.next.prev = destination  # reconnect
            destination.prev.next = destination
        else:  # the node we're going to add things in already exists
            destination = origin_bucket.prev
        if origin_bucket is not self.inf_node:  # remove from previous if needed
            origin_bucket.keys.remove(key)
            if len(origin_bucket.keys) == 0:  # remove
                origin_bucket.next.prev = origin_bucket.prev
                origin_bucket.prev.next = origin_bucket.next
        destination.keys.add(key)
        self.key_to_bucket[key] = destination
        return

    def getMaxKey(self) -> str:
        max_node = self.inf_node.prev
        if max_node.val == 0:
            return ''
        return list(max_node.keys)[0]

    def getMinKey(self) -> str:
        min_node = self.zero_node.next
        if min_node.val == float('inf'):
            return ''
        return list(min_node.keys)[0]


'''
solution: use iter, set dummy value
oh! seems iter is faster than converting the whole set into list
'''


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val
        self.keys = set()


class AllOne:

    def __init__(self):
        self.key_to_bucket = {}  # key -> DL node
        self.zero_node = ListNode(0, None, None)
        self.inf_node = ListNode(inf, None, None)
        self.zero_node.next = self.inf_node
        self.inf_node.prev = self.zero_node
        self.zero_node.keys.add('')
        self.inf_node.keys.add('')
        return

    def inc(self, key: str) -> None:
        origin_bucket = self.key_to_bucket.get(key, self.zero_node)
        if origin_bucket.next.val != origin_bucket.val+1:  # there's no node for the new count number, create one
            destination = ListNode(origin_bucket.val+1, origin_bucket, origin_bucket.next)
            destination.next.prev = destination  # reconnect
            destination.prev.next = destination
        else:  # the node we're going to add things in already exists
            destination = origin_bucket.next

        if origin_bucket is not self.zero_node:  # remove from previous if needed
            origin_bucket.keys.remove(key)
            if len(origin_bucket.keys) == 0:  # remove
                origin_bucket.prev.next = origin_bucket.next
                origin_bucket.next.prev = origin_bucket.prev
        destination.keys.add(key)
        self.key_to_bucket[key] = destination
        return

    def dec(self, key: str) -> None:
        origin_bucket = self.key_to_bucket.get(key, self.inf_node)
        if origin_bucket.prev.val != origin_bucket.val-1:  # there's no node for the new count number, create one
            destination = ListNode(origin_bucket.val-1, origin_bucket.prev, origin_bucket)
            destination.next.prev = destination  # reconnect
            destination.prev.next = destination
        else:  # the node we're going to add things in already exists
            destination = origin_bucket.prev
        if origin_bucket is not self.inf_node:  # remove from previous if needed
            origin_bucket.keys.remove(key)
            if len(origin_bucket.keys) == 0:  # remove
                origin_bucket.next.prev = origin_bucket.prev
                origin_bucket.prev.next = origin_bucket.next
        destination.keys.add(key)
        self.key_to_bucket[key] = destination
        return

    def getMaxKey(self) -> str:
        max_node = self.inf_node.prev
        return next(iter(max_node.keys))

    def getMinKey(self) -> str:
        min_node = self.zero_node.next
        return next(iter(min_node.keys))
