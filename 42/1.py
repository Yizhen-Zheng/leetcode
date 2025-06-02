
class Solution:
    # stack
    def trap(self, height: list[int]) -> int:
        result = 0
        max_left = [height[0]]
        max_right = [height[-1]]
        # prepare:
        for i in range(len(height)-2, 0, -1):
            # append highest
            max_right.append(height[i] if height[i] >
                             max_right[-1]else max_right[-1])
        for i in range(1, len(height)-1):
            current_height = height[i]
            left_highest = max_left[-1]
            right_highest = max_right.pop()
            current_water = max(
                min(left_highest, right_highest)-current_height, 0)
            # if current itself is highest, current water will be 0
            result += current_water
            max_left.append(current_height if current_height >
                            max_left[-1]else max_left[-1])

        # for left and right most, no water
        # for each column between, the rain water above the column depends on:
        # left, right height
        # c < math.min(left,right): has water
        # else: no water

        return result


t1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution().trap(t1)
print(s)
