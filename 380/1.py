import random


class RandomizedSet:
    '''
    10:14-11:14
    val: int
    maybe a dict/bitset and size
    val has minus
    naive: set, list(bucket)[random.randint(0,len(bucket))]
    len(vals): contains both useful val, and garbage(removed)
    '''

    def __init__(self):
        self.size = 0
        self.vals = []
        self.lookup = {}  # use a general dict instead
        # neg_idx = [-1] * (1 << 32) # will cause memory err
        # pos_idx = [-1]*(1 << 32)
        # self.lookup.append(neg_idx)
        # self.lookup.append(pos_idx)
        return

    def insert(self, val: int) -> bool:
        if val in self.lookup:  # already exist
            return False
        # get tail position, first_grabage position is self.size
        if self.size >= len(self.vals):   # no garbage
            # e,g, size 0, or not removed yet
            self.vals.append(val)  # just add
        else:  # add to tail
            self.vals.append(val)
            # swap with first garbage
            self.vals[-1], self.vals[self.size] = self.vals[self.size], self.vals[-1]
        self.lookup[val] = self.size
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.lookup:
            return False
        self.size -= 1  # know size points to last useful val
        pos = self.lookup[val]  # pos to remove
        self.vals[pos], self.vals[self.size] = self.vals[self.size], self.vals[pos]
        changed_elem = self.vals[pos]  # now an useful val is on pos
        self.lookup[changed_elem] = pos
        self.lookup.pop(val)
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, self.size-1)
        return self.vals[idx]


class RandomizedSet:
    '''
    cleanup
    '''

    def __init__(self):
        self.vals = []
        self.lookup = {}  # size is len(lookup)
        return

    def insert(self, val: int) -> bool:
        if val in self.lookup:  # already exist
            return False

        self.lookup[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.lookup:
            return False

        pos = self.lookup[val]  # get pos, remove from hashmap
        self.vals[pos], self.vals[-1] = self.vals[-1], self.vals[pos]  # swap
        changed_elem = self.vals[pos]  # now an useful val is on pos
        self.lookup[changed_elem] = pos
        # if pop earlier, need to check if removed is the only elem(accidentally add back)
        self.lookup.pop(val)  # remove immediately, keep all values without garbage
        self.vals.pop()  # later remove, prevent empty arr
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.vals)-1)
        return self.vals[idx]
