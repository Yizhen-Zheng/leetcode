'''
heap up and heap down: O(n * logn)
sort: O(nlogn)(total n elems, every heap down elem is logn)
'''


class min_heap:
    def __init__(self, arr=[]):
        self.heap = []  # a min heap
        if arr:
            self.heap = self  # heapify down

        self.size = len(self.heap)

    def heap_down(self):
        heap = self.heap
        if not heap:  # after pop the only elem in the heap, there'll be no elem to swap
            return
        bound = self.size
        idx = 0
        while idx < bound:
            l_idx = idx*2+1
            r_idx = min(bound-1, idx*2+2)
            if l_idx >= bound:
                return idx
            smaller_idx = l_idx if heap[l_idx] < heap[r_idx] else r_idx
            if heap[idx] <= heap[smaller_idx]:  # already put in correct position
                return idx
            heap[idx], heap[smaller_idx] = heap[smaller_idx], heap[idx]  # swap
            idx = smaller_idx
        return idx

    def heap_up(self):  # O(logn)
        heap = self.heap

        idx = len(heap)-1  # the new added elem
        while idx > 0:  # only need nums[i]<nums[parent_idx], since (0-1)/2==0
            parent_idx = (idx-1)//2
            if heap[parent_idx] <= heap[idx]:
                return idx
            heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
            idx = parent_idx
        return idx

    def push_to_heap(self, num):
        heap = self.heap
        heap.append(num)
        self.size += 1
        self.heap_up()

        return

    def pop_head(self):
        heap = self.heap
        heap[0], heap[-1] = heap[-1], heap[0]  # swap prepare to pop minimum
        head = heap.pop()
        self.size -= 1
        self.heap_down()
        return head

    def sort(self):
        heap = [n for n in self.heap]
        size = self.size
        sorted_arr = []
        while self.size:
            sorted_arr.append(self.pop_head())
        self.heap = heap
        self.size = size
        return sorted_arr

    def heapify_top_down(self, arr):
        # O(nlogn)
        for i in range(1, len(arr)):  # skip 0
            idx = i
            while idx > 0:  # heap up
                parent = (idx-1)//2
                if arr[parent] <= arr[idx]:
                    break
                arr[idx], arr[parent] = arr[parent], arr[idx]
                idx = parent
        return

    def heapify_bottom_up(self, arr):
        n = len(arr)
        for i in range(n//2-1, -1, -1):
            idx = i
            smallest_idx = idx
            while idx < n:  # heap down
                left = idx*2+1
                if left < n and arr[left] < arr[smallest_idx]:
                    smallest_idx = left

                right = idx*2+2
                if right < n and arr[right] < arr[smallest_idx]:
                    smallest_idx = right
                if smallest_idx == idx:
                    break
                arr[idx], arr[smallest_idx] = arr[smallest_idx], arr[idx]
                idx = smallest_idx

        return
#


class max_heap:
    def __init__(self, arr=[]):
        self.heap = []  # a min heap
        if arr:
            # self.heapify_bottom_up(arr)
            self.heapify_top_down(arr)
            self.heap = arr

        self.size = len(self.heap)

    def heap_down(self):
        heap = self.heap
        if not heap:  # after pop the only elem in the heap, there'll be no elem to swap
            return
        bound = self.size
        idx = 0
        while idx < bound:
            l_idx = idx*2+1
            r_idx = min(bound-1, idx*2+2)
            if l_idx >= bound:
                return idx
            greater_idx = l_idx if heap[l_idx] > heap[r_idx] else r_idx
            if heap[idx] >= heap[greater_idx]:  # already put in correct position
                return idx
            heap[idx], heap[greater_idx] = heap[greater_idx], heap[idx]  # swap
            idx = greater_idx
        return idx

    def heap_up(self):  # O(logn)
        heap = self.heap

        idx = len(heap)-1  # the new added elem
        while idx > 0:  # only need nums[i]<nums[parent_idx], since (0-1)/2==0
            parent_idx = (idx-1)//2
            if heap[parent_idx] >= heap[idx]:
                return idx
            heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
            idx = parent_idx
        return idx

    def push_to_heap(self, num):
        heap = self.heap
        heap.append(num)
        self.size += 1
        self.heap_up()

        return

    def pop_head(self):
        heap = self.heap
        heap[0], heap[-1] = heap[-1], heap[0]  # swap prepare to pop minimum
        head = heap.pop()
        self.size -= 1
        self.heap_down()
        return head

    def sort(self):
        origin_heap = [n for n in self.heap]
        heap = self.heap
        size = self.size
        while self.size:
            heap[0], heap[self.size-1] = heap[self.size-1], heap[0]
            self.size -= 1
            self.heap_down()
        sorted_arr = self.heap
        self.heap = origin_heap
        self.size = size
        return sorted_arr

    def heapify_top_down(self, arr):
        # O(nlogn)
        for i in range(1, len(arr)):
            idx = i
            while idx > 0:  # heap up
                parent = (idx-1)//2
                if arr[parent] >= arr[idx]:
                    break
                arr[idx], arr[parent] = arr[parent], arr[idx]
                idx = parent
        return

    def heapify_bottom_up(self, arr):
        n = len(arr)
        for i in range(n//2-1, -1, -1):
            idx = i
            largest_idx = idx
            while idx < n:  # heap down
                left = idx*2+1
                if left < n and arr[left] > arr[largest_idx]:
                    largest_idx = left

                right = idx*2+2
                if right < n and arr[right] > arr[largest_idx]:
                    largest_idx = right
                if largest_idx == idx:
                    break
                arr[idx], arr[largest_idx] = arr[largest_idx], arr[idx]
                idx = largest_idx

        return


def test_min():
    my_heap = min_heap()
    my_heap.push_to_heap(1)
    my_heap.push_to_heap(1)
    my_heap.push_to_heap(0)
    my_heap.push_to_heap(7)
    my_heap.push_to_heap(0)
    my_heap.push_to_heap(4)
    my_heap.push_to_heap(2)
    # print(my_heap.heap)
    n = my_heap.pop_head()
    assert n == 0
    sorted_arr = my_heap.sort()
    # print(sorted_arr)
    arr = [2, 6, 1, 4, 0, 5, 7]
    my_heap.heapify_top_down(arr)
    print(arr)
    arr = [2, 6, 1, 4, 0, 5, 7]
    my_heap.heapify_bottom_up(arr)
    print(arr)


def test_max():
    my_heap = max_heap()
    my_heap.push_to_heap(1)
    my_heap.push_to_heap(7)
    my_heap.push_to_heap(0)
    my_heap.push_to_heap(4)
    my_heap.push_to_heap(2)
    # print(my_heap.heap)
    n = my_heap.pop_head()
    assert n == 7
    sorted_arr = my_heap.sort()
    my_heap.push_to_heap(11)
    sorted_arr = my_heap.sort()
    # print(sorted_arr)
    # print(my_heap.heap)
    my_heap.push_to_heap(3)
    # print(my_heap.heap)
    arr = [2, 6, 1, 4, 0, 5, 7]
    my_heap.heapify_top_down(arr)
    # print(arr)
    arr = [2, 6, 1, 4, 0, 5, 7]
    my_heap.heapify_bottom_up(arr)
    print(arr)


test_min()
test_max()
