class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        '''
        try brute-force first
        expand around center
        t: O(n^2)
        s: O(1)
        '''
        max_area = 0
        n = len(heights)
        for i, h in enumerate(heights):
            l, r = i-1, i+1
            while r < n and h <= heights[r]:
                r += 1
            while l > -1 and h <= heights[l]:
                l -= 1
            max_area = max(max_area, h*(r-l-1))
        return max_area

    def largestRectangleArea(self, heights: list[int]) -> int:
        '''
        revuew 7:21-9:37
        should allow [1,1,1,1...]
        (indices,height), track expansion len correctly
        how to handle expand to both left and right?
        t: O(n)(every elems in and out exactly twice)
        s: O(n)
        '''
        s = []  # dummy?
        n = len(heights)
        max_area = 0
        for i, cur_h in enumerate(heights):
            # cur expands to left
            while s and cur_h < s[-1][1]:
                pos, height = s.pop()
                left_bound = -1 if not s else s[-1][0]
                max_area = max(max_area, (i-left_bound-1)*height)
            s.append((i, cur_h))
        # expand to right
        while s:
            i, cur_h = s.pop()
            # cur can have gap between cur and prev
            # the gap len is cur can expand to left
            left_bound = -1 if not s else s[-1][0]
            max_area = max(max_area, (n-left_bound-1)*cur_h)
        return max_area

    def largestRectangleArea(self, heights: list[int]) -> int:
        '''
        space optimize: no need for h
        add dummy to simplify
        '''
        s = []  # dummy?
        n = len(heights)
        max_area = 0
        for i, cur_h in enumerate(heights):
            # expands to left(prev) and right(cur)
            while s and cur_h < heights[s[-1]]:
                pos = s.pop()
                left_bound = -1 if not s else s[-1]
                max_area = max(max_area, (i-left_bound-1)*heights[pos])
            s.append(i)
        # expand to right
        while s:
            i = s.pop()
            # cur can have gap between cur and prev
            # the gap len is cur can expand to left
            left_bound = -1 if not s else s[-1]
            max_area = max(max_area, (n-left_bound-1)*heights[i])
        return max_area

    def largestRectangleArea(self, heights: list[int]) -> int:
        '''
        add dummy to simplify
        '''
        s = []
        # n = len(heights)
        heights.append(0)  # dummy, filter out all elems left(idx if n)
        max_area = 0
        for i, cur_h in enumerate(heights):
            # expands to left(prev) and right(cur)
            while s and cur_h < heights[s[-1]]:
                pos = s.pop()
                # cur can have gap between cur and prev
                # the gap len is cur can expand to left
                left_bound = -1 if not s else s[-1]
                # right bound: expand to current i(i will always meet rear immediately once rear > cur)
                max_area = max(max_area, (i-left_bound-1)*heights[pos])
            s.append(i)
        return max_area


t = [2, 1, 5, 6, 2, 3]
# t = [2, 1]
t = [2, 1, 2]
# t = [4, 3, 4]
# t = [2, 2, 2]
# t = [5, 4, 1, 2]
r = Solution().largestRectangleArea(t)
print(r)
