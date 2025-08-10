from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''7min'''
        if len(s) != len(t):
            return False
        arr = [0]*123
        for c in s:
            arr[ord(c)] += 1
        for c in t:
            arr[ord(c)] -= 1
            if arr[ord(c)] < 0:
                return False

        return True

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
