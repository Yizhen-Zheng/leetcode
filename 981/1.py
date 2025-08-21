from collections import defaultdict
import heapq
import bisect


class TimeMap:
    '''
    10:12-10:31
    brute-force: default dict with max heap, or bisect? seems bisect and heap both search in logn
    but bisect need O(n) to insert 
    find key
    set: t:O(logn),s:O(1)
    get: t:O(logn),s:O(n)
    '''

    def __init__(self):
        self.storage = defaultdict(list)
        self.seen = set()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key, value, timestamp) in self.seen:
            return
        bucket = self.storage[key]  # get corresponding bucket
        heapq.heappush(bucket, (-timestamp, value))  # max heap,O(logn)

    def get(self, key: str, timestamp: int) -> str:
        bucket = self.storage[key].copy()
        while bucket:
            ts, val = bucket[0]  # max ts
            if -ts <= timestamp:  # within ts
                return val
            heapq.heappop(bucket)  # next biggest ts
        return ''


class TimeMap:
    '''
    OHH! All the timestamps timestamp of set are strictly increasing.
    use Bisect
    set: t: O(1)
    get: t: O(logn)
    '''

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bucket = self.storage[key]  # get corresponding bucket
        bucket.append(((timestamp, value)))  # O(1)

    def get(self, key: str, timestamp: int) -> str:
        '''
        bi left
        insert position = idx, 
        num <= arr[idx]
        0, 1, 2, insert 2':
        0, 1, 2', 2
        '''
        bucket = self.storage[key]
        idx = bisect.bisect_left(bucket, timestamp+1, key=lambda x: x[0])-1
        print(idx)
        if idx < 0:
            return ''
        return bucket[idx][1]

    def get(self, key: str, timestamp: int) -> str:
        '''
        bi left, manual
        insert position = idx, 
        num <= arr[idx]
        0, 1, 2, insert 2':
        0, 1, 2', 2
        a[lo:inters_idx], all elems strictly < target, 
        a[inters_idx:hi],all elems >= target 
        '''
        bucket = self.storage[key]

        def bl(arr, num):
            n = len(arr)
            l, r = 0, n  # NOTE init r as n handle edge case
            while l < r:
                m = l+(r-l)//2
                m_val = arr[m][0]
                if m_val < num:  # l include elem < target
                    l = m+1
                else:
                    r = m
            return l
        idx = bl(bucket, timestamp+1)-1
        print(idx)
        if idx < 0:
            return ''
        return bucket[idx][1]

    def get(self, key: str, timestamp: int) -> str:
        '''
        bi right
        insert position = idx, 
        num >= arr[idx]
        0, 1, 2, insert 2':
        0, 1, 2, 2'
        '''
        bucket = self.storage[key]
        idx = bisect.bisect_right(bucket, timestamp, key=lambda x: x[0])
        print(idx)
        if idx < 1:
            return ''
        return bucket[idx-1][1]

    def get(self, key: str, timestamp: int) -> str:
        '''
        bi right manual
        insert position = idx, 
        num >= arr[idx]
        0, 1, 2, insert 2':
        0, 1, 2, 2'
        a[lo:inters_idx], all elems <= target,
        a[inters_idx:hi],all elems strictly > target

        '''
        bucket = self.storage[key]

        def br(arr, num):
            n = len(arr)
            l, r = 0, n
            while l < r:
                m = l+(r-l)//2
                m_val = arr[m][0]
                if m_val <= num:  # l include elem <= target
                    l = m+1
                else:
                    r = m
            return l
        idx = br(bucket, timestamp)
        print(idx)
        if idx < 1:
            return ''
        return bucket[idx-1][1]
