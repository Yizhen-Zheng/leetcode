class Solution:

    def largestRectangleAreaI(self, heights: list[int]) -> int:
        # '''
        # brute force
        # t:O(n^3)
        # s:O(1)
        # 8min
        # '''
        # n = len(heights)
        # max_area = 0
        # for i in range(n):
        #     for j in range(i, -1, -1):
        #         low = min(heights[j:i+1])
        #         area = (i-j+1)*low
        #         max_area = max(max_area, area)
        # return max_area
        '''
        brute foece II
        remember cur_min_height
        maybe s and e
        8min + ? (about 18 min)
        t: O(n^2)
        s: O(n^2)
        '''
        n = len(heights)
        dp = [[-1]*n for _ in range(n)]
        # so far min height and included numbers
        max_area = 0
        for start in range(0, n):
            cur_low = heights[start]
            for end in range(start, n):
                cur_low = min(cur_low, heights[end])
                dp[start][end] = cur_low*(end-start+1)
                max_area = max(max_area, dp[start][end])
        [print(l)for l in dp]
        return max_area

    def largestRectangleArea(self, heights: list[int]) -> int:
        '''
        try evolve 
        we don't know what's there between fron and end
        maybe first loop to mark low
        so far smallest element's idx
        try divide and conquer(O(nlogn))
        not work:
        ------------------------------------------
        n = len(heights)
        def divide(s, e):
            if s >= e:
                return (s, s)  # for individual elem, largest is itself
            lr = [0]*(e-s+1)
            lr[0] = s
            rl = [0]*(e-s+1)
            rl[n-1] = e
            for i in range(s+1, e+1):
                if heights[lr[i-1]] > heights[i]:
                    lr[i] = i
                else:
                    lr[i] = lr[i-1]
            for i in range(e-1, s-1, -1):
                if heights[rl[i+1]] > heights[i]:
                    rl[i] = i
                else:
                    rl[i] = rl[i+1]
            m = (s+e)//2
            merged = (e-s+1)*heights[lr[e]]
        ------------------------------------------
        follow solution:
        use greedy to implement bi-direction exploration
        '''
        n = len(heights)

        def merge(s, m, e):
            l, r = m, m+1  # expand start
            max_area = 0
            low = min(heights[l], heights[r])  # smaller in 2 bars
            while l >= s and r <= e:
                low = min(low, heights[l], heights[r])
                max_area = max(max_area, (r-l+1)*low)
                if l == s:  # expand single direction if one reached bound
                    r += 1
                elif r == e:
                    l -= 1
                else:
                    if heights[l-1] > heights[r+1]:
                        l -= 1
                    else:
                        r += 1
            return max_area

        def divide(s, e):
            if s >= e:
                return heights[s]  # only one elem
            m = (s+e)//2
            left = divide(s, m)
            right = divide(m+1, e)
            l_or_r_max = max(left, right)
            merged_max = merge(s, m, e)
            return max(l_or_r_max, merged_max)
        return divide(0, n-1)

    def largestRectangleArea(self, heights: list[int]) -> int:
        '''
        for each bar i, calculate how far it can expand if use it as center
        how: min of its left low and its right low
        NOTE bound is not proved consistent
        [1,2,1]: 
        [0,1,1] <-false , should be [0,1,0], sence idx=2 can expand to idx=0

        '''
        n = len(heights)
        lr = [-1]*n  # how far one can expand to left
        rl = [n]*n  # how far one can expand to right
        for i in range(1, n):
            bound = i-1  # start from itself
            # current is lower OR EQUAL, use neighbor's boundary
            while bound >= 0 and heights[i] <= heights[bound]:
                bound = lr[bound]
            lr[i] = bound

        for i in range(n-2, -1, -1):
            bound = i+1
            while bound < n and heights[i] <= heights[bound]:
                bound = rl[bound]
            rl[i] = bound
        max_area = 0
        for i in range(n):
            l_bound = lr[i]
            r_bound = rl[i]
            h = heights[i]
            length = r_bound-l_bound-1
            area = h*length
            max_area = max(max_area, area)
        return max_area

    def largestRectangleArea(self, heights: list[int]) -> int:
        '''
        monotonic stack
        the idea: if a smaller elem comes, we should remove larger ones. 
            e,g, [2,1], 2(the height) won't have effect on result
        '''
        n = len(heights)
        max_area = 0
        # heights.append(0)  # dummy value to handle last remain in stack
        stack = []  # [idx,h]
        for cur_i in range(n):
            cur_h = heights[cur_i]
            last_idx = cur_i
            while stack and stack[-1][1] >= cur_h:
                last_idx, last_h = stack.pop()
                l = cur_i-last_idx
                max_area = max(max_area, l*last_h)
            stack.append((last_idx, cur_h))
        while stack:
            start_i, h = stack.pop()
            max_area = max(max_area, (n-start_i)*h)
        return max_area

    def largestRectangleArea(self, heights: list[int]) -> int:
        '''
        another stack
        reduce the (idx,h) by adding a dummy start
        and use last idx in stack after poping to calculate width
        it's fine if origin heights ends with 0, it doesn't change the res
        why width use i-stack[-1]-1 instead of last_i=stack[-1]:
            coz bar at last_i potentially extend to both sides
            [2,5,3,4,2]
             0 1 2 3 4
            when i = 4: stack=[-1,0,2,3]
                pop idx=3, area=4, stack=[-1,0,2]
                pop idx=2, the height=3 can extend to both 5 and 4, stack=[-1,0]
                    so width is 4-0-1=3
                    although idx=1(5) is not in stack, it is taken into consider

        why append 0 at last:
        heights=[1,2,3,4,5,0], 
                 0 1 2 3 4
        when idx=4, stack=[-1,0,1,2,3,4], haven't calculate any val
        idx=5, all elem will be poped
        '''
        heights.append(0)
        n = len(heights)
        stack = [-1]
        max_area = 0
        for i in range(n):
            while stack and stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                last_i = stack.pop()
                last_h = heights[last_i]
                extend_to = stack[-1]
                width = i-extend_to-1
                area = last_h*width
                max_area = max(max_area, area)
            stack.append(i)
        heights.pop()  # remove side effect
        return max_area


t = [1, 4, 2, 5]
t = [1, 1, 6, 5, 2]
# t = [2, 1, 5, 6, 2, 3]
# t = [1, 1]
t = [1, 2, 3, 4, 5]
r = Solution().largestRectangleArea(t)
print(r)
