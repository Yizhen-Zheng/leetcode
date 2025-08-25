class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        '''
        9:58-10:27
        looks like dp
        won't have case like c=[0],t=[2]
        no use time limit
        if it's dp: col: elems, rows: target//smallest_elem + 1
        brute-force: enumerate combinations
        t: O(n^n)
        s: O(target//min_num+1), stack deptth
        '''
        # if min_num > target or min_num == 0: # optional: handle 0
        #     return []
        ans = set()
        min_num = min(candidates)
        upper_bound = target//min_num+1

        def rec(cur_sum: int, cur_path: list[int]):
            if cur_sum == target:
                ans.add(tuple(sorted(cur_path)))
                return
            if cur_sum > target:
                return
            for num in candidates:
                cur_path.append(num)
                rec(cur_sum+num, cur_path)
                cur_path.pop()
        rec(0, [])
        list_ans = list(map(list, ans))
        return list_ans

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        '''
        10:28-11:08, try backtrace
        maybe first sort?
        max heap?
        hashmap? (distinct + small size)
        if cur_goal<min_num: return
        maybe only travel elems >= cur
        t: O(2^n) (max tree height: n, each layer multiply by n)
        s: O(target//min_num+1), stack depth like c=[2],t=8
        '''
        ans = []
        candidates.sort()
        n = len(candidates)
        # min_num = min(candidates)

        def rec(cur_num_idx: int, cur_sum: int, cur_path: list[int]):
            if cur_sum == target:
                ans.append(cur_path.copy())
                return
            if cur_sum > target:
                return
            for next_idx in range(cur_num_idx, n):
                num = candidates[next_idx]
                cur_path.append(num)
                rec(next_idx, cur_sum+num, cur_path)
                cur_path.pop()
        rec(0, 0, [])
        return ans

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        '''
        solution
        this prunes both lower and higher
        '''
        n = len(candidates)
        res = []
        candidates.sort()

        def rec(cur_path: list, remain: int, idx: int):
            if remain == 0:
                res.append(cur_path.copy())
                return
            for next_idx in range(idx, n):
                num = candidates[next_idx]
                if num > remain:  # prune upper
                    return
                cur_path.append(num)
                rec(cur_path, remain-num, next_idx)
                cur_path.pop()
        rec([], target, 0)
        return res


t = ([2, 3, 6, 7], 7)
t = ([9, 3, 6, 7], 12)
r = Solution().combinationSum(t[0], t[1])
print(r)
