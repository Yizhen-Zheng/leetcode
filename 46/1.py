class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        '''
        11:41-11:48
        all posible perms
        nums len < 6! 
        t: O(n^2), loop all nums
        s: O(n), stack depth
        also can use set('#' -> add to set, remove from set)

        '''
        n = len(nums)
        perms = []

        def rec(cur_path: list[int]):
            if len(cur_path) == n:
                perms.append(cur_path.copy())
            for i in range(n):
                if nums[i] != '#':
                    cur_path.append(nums[i])
                    nums[i] = '#'
                    rec(cur_path)
                    nums[i] = cur_path.pop()
            return
        rec([])
        return perms

    def permute(self, nums: list[int]) -> list[list[int]]:
        '''
        solution:
        also can use idx:
        nums[start],nums[next_i]=nums[next_i],nums[start], 
        so next rec always loop from unvisited(start + 1, path)
        then change them back
        t: O(n^2) (tree size)(n^0 -> n^1 -> ... n^n)
        s: O(n), stack depth
        '''
        n = len(nums)
        perms = []

        def rec(change_pos: int):
            if change_pos == n-1:
                perms.append(nums[:])
            for i in range(change_pos, n):
                nums[change_pos], nums[i] = nums[i], nums[change_pos],
                rec(change_pos+1)
                nums[change_pos], nums[i] = nums[i], nums[change_pos],
            return
        rec(0)
        return perms
