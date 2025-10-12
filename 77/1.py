class Solution:
    '''  
    basic formula to count all combination:     
    com = 1
    for i in range(k+1, n+1):
        com *= i
    for i in range(1, k+1):
        com /= i
    return int(com)

    permutation:
    perm = 1
    for i in range(k+1, n+1):
        perm *= i
    return perm
    '''

    def combine(self, n: int, k: int) -> list[list[int]]:
        '''
        9:24 - 11:21
        range: 1-n, n numbers, choose k
        t: O(2^n)
        trie
        '''
        ans = []

        def rec(path: list[int]):
            if len(path) == k:
                ans.append(path[:])
                return
            start = path[-1] if path else 0
            for i in range(start+1, n+1):
                path.append(i)
                rec(path)
                path.pop()
            return
        rec([])
        return ans

    def combine(self, n: int, k: int) -> list[list[int]]:
        '''
        ans:
        '''
        ans = []

        def rec(s: int, path: list[int]):
            if len(path) == k:
                ans.append(path[:])
                return
            if s == n+1:
                return
            for i in range(s, n+1):
                path.append(i)
                rec(i+1, path)
                path.pop()
        rec(1, [])
        return ans
