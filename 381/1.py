from collections import defaultdict
import random


class RandomizedCollection:
    '''
    6:43-
    maybe timestamp?
    what will happen if same val, same pos, but actually different?
    '''

    def __init__(self):
        self.map = defaultdict(set)
        self.arr = []
        return

    def insert(self, val: int) -> bool:
        pos = len(self.arr)
        self.arr.append(val)
        if val in self.map and len(self.map[val]) > 0:
            self.map[val].add(pos)
            return False
        self.map[val].add(pos)
        return True

    def remove(self, val: int) -> bool:
        if len(self.map[val]) < 1:
            return False
        n = len(self.arr)
        if val == self.arr[-1]:
            self.map[val].remove(n-1)
            self.arr.pop()
            return True
        pos = self.map[val].pop()  # convert to arr SET CAN POP!
        changed_val = self.arr[len(self.arr)-1]
        self.arr[pos], self.arr[-1] = self.arr[-1], self.arr[pos]
        self.map[changed_val].remove(len(self.arr)-1)
        self.map[changed_val].add(pos)
        self.arr.pop()
        return True

    def getRandom(self) -> int:

        return self.arr[random.randint(0, len(self.arr)-1)]

        # Your RandomizedCollection object will be instantiated and called as such:
        # obj = RandomizedCollection()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()
