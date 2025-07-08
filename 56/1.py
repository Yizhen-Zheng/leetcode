from typing import List


class Solution:
    def mergeI(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        look at head(arr[0][0]), look at tail(arr[-1][-1]), -> if no need to merge
        begin<=end
        n*logn: faster than n, smaller than n^2
        '''

        def merge_sort(intervals: list[list[int]]):
            if len(intervals) <= 1:
                return intervals
            mid = len(intervals)//2
            left = merge_sort(intervals[:mid])
            right = merge_sort(intervals[mid:])
            l_ptr = 0
            r_ptr = 0
            sorted_list = []
            while l_ptr < len(left) and r_ptr < len(right):
                if left[l_ptr][0] < right[r_ptr][0]:
                    sorted_list.append(left[l_ptr])
                    l_ptr += 1
                elif left[l_ptr][0] > right[r_ptr][0]:
                    sorted_list.append(right[r_ptr])
                    r_ptr += 1
                else:
                    if left[l_ptr][1] > right[r_ptr][1]:
                        sorted_list.append(right[r_ptr])
                        r_ptr += 1
                    elif left[l_ptr][1] < right[r_ptr][1]:
                        sorted_list.append(left[l_ptr])
                        l_ptr += 1
                    else:
                        sorted_list.append(left[l_ptr])
                        l_ptr += 1
                        r_ptr += 1
            if l_ptr < len(left):
                sorted_list += left[l_ptr:]
            if r_ptr < len(right):
                sorted_list += right[r_ptr:]
            return sorted_list

        intervals = merge_sort(intervals)

        if len(intervals) <= 1:
            return intervals
        n = len(intervals)
        merged = [intervals[0]]
        idx = 1
        while idx < n:
            cur_head, cur_tail = merged[-1]
            next_head, next_tail = intervals[idx]

            if cur_tail >= next_head:
                # reached intervals[-1], might be able to merge or not
                new_tail = next_tail if next_tail > cur_tail else cur_tail
                merged[-1] = [cur_head, new_tail]

            else:
                merged.append(intervals[idx])
            idx += 1
        return merged

    def mergeII(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        look at head(arr[0][0]), look at tail(arr[-1][-1]), -> if no need to merge
        begin<=end
        n*logn: faster than n, smaller than n^2
        '''

        def merge_sort(intervals: list[list[int]]):
            if len(intervals) <= 1:
                return intervals
            mid = len(intervals)//2
            left = merge_sort(intervals[:mid])
            right = merge_sort(intervals[mid:])
            l_ptr = 0
            r_ptr = 0
            sorted_list = []
            while l_ptr < len(left) and r_ptr < len(right):
                if left[l_ptr][0] < right[r_ptr][0]:
                    sorted_list.append(left[l_ptr])
                    l_ptr += 1
                elif left[l_ptr][0] > right[r_ptr][0]:
                    sorted_list.append(right[r_ptr])
                    r_ptr += 1
                else:
                    merged_elem = [left[l_ptr][0], max(left[l_ptr][1], right[r_ptr][1])]
                    sorted_list.append(merged_elem)
                    l_ptr += 1
                    r_ptr += 1
            if l_ptr < len(left):
                sorted_list += left[l_ptr:]
            if r_ptr < len(right):
                sorted_list += right[r_ptr:]
            return sorted_list

        intervals = merge_sort(intervals)

        if len(intervals) <= 1:
            return intervals
        n = len(intervals)
        merged = [intervals[0]]
        idx = 1
        while idx < n:
            cur_head, cur_tail = merged[-1]
            next_head, next_tail = intervals[idx]

            if cur_tail >= next_head:
                # reached intervals[-1], might be able to merge or not
                new_tail = next_tail if next_tail > cur_tail else cur_tail
                merged[-1] = [cur_head, new_tail]

            else:
                merged.append(intervals[idx])
            idx += 1
        return merged

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        look at head(arr[0][0]), look at tail(arr[-1][-1]), -> if no need to merge
        begin<=end
        n*logn: faster than n, smaller than n^2
        '''

        intervals = sorted(intervals, key=lambda x: x[0])

        if len(intervals) <= 1:
            return intervals
        n = len(intervals)
        merged = [intervals[0]]
        idx = 1
        while idx < n:
            cur_tail = merged[-1][-1]
            next_head, next_tail = intervals[idx]

            if cur_tail >= next_head:
                new_tail = max(next_tail, cur_tail)
                merged[-1][-1] = new_tail
            else:
                merged.append(intervals[idx])
            idx += 1
        return merged


t = [[0, 5], [1, 1]]
t = [[1, 2], [0, 2], [0, 6]]
# t = [[1, 1], [2, 2], [5, 6]]
r = Solution().merge(t)
print(r)
