# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        binary search
        left boundary
        3min+4min(dry run )
        '''
        l, r = 1, n
        while l < r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m
            else:
                l = m+1
        return l
