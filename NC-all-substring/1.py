class Solution:
    '''
    the 1st and 2ed both travel the whole n^2 binary tree!
    but 1st uses less stack sizess
    '''
    def allSubstring(s: str):
        '''
        enumerate all combinations
        O(2^n)(2^n * n), n for build a substr(str concat)
        about 7 min?
        '''
        ans = {''}
        for c in s:
            for elem in list(ans):
                ans.add(elem+c)
        return list(ans)

    def allSubstring(s: str):
        n = len(s)
        ans = set()

        def dfs(idx, path: list[str]):
            if idx == n:
                ans.add(''.join(path))
                return
            path.append(s[idx])
            dfs(idx+1, path)
            path.pop()
            dfs(idx+1, path)
            return
        dfs(0, [])
        return list(ans)
