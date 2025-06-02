
class Solution:
    # greedy, 2 pointer
    # if ,
    def trap(self, height: list[int]) -> int:
        result = 0
        left = 1
        right = len(height)-2
        max_left = height[0]
        max_right = height[-1]
        while left <= right:
            # for the 0th iterate:
            # we' known ml, mr at left most, right most
            # the less one of the 2 sides will decide its inner neighbor's water line
            # the opposite of min(ml, mr)'s realistic max remains unknown
            # so, we move the less side each step,
            # since we can only confirm that side's water
            # min(max_left, max_right) - current
            if height[left] < height[right]:
                # the moving pointer step's position (before or after calculating current water) doesn't effect much
                # but moving after will include 2 ends, which will take 2 more steps to add 0

                # or think this way:
                # we move pointer after comparing which side is smaller
                # bcz we want to use the smaller side will decide its inner neighbor's water, not the greater side
                # [2,1,...,4,3]
                #    l       r
                # 1's water depends on 2, not 3,
                # [2,1,...,4,5]
                # if we look at greater side, 4 could have left max greater or less than 4
                # but 1 has at least 2,
                result += max(min(max_left, max_right)-height[left], 0)
                max_left = max(max_left, height[left])
                left += 1
            else:
                result += max(min(max_right, max_left)-height[right], 0)
                max_right = max(max_right, height[right])
                right -= 1
        return result

    def trap1(self, height: list[int]) -> int:
        result = 0
        left = 0
        right = len(height)-1
        max_left = height[0]
        max_right = height[-1]
        while left < right:
            # left < right: need cooperate with move pointer first, then do the calculate
            # the last iteration would overlap at some opint,
            # but since the previous pointer has updated the max height of the end point, it would add 0,
            if height[left] < height[right]:
                left += 1
                max_left = max(max_left, height[left])
                result += max(max_left-height[left], 0)
            else:
                right -= 1
                max_right = max(max_right, height[right])
                result += max(max_right-height[right], 0)
        return result


t1 = [2, 1, 0,  3, 1, 2]
t2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution().trap(t2)
print(s)
