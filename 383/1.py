from collections import Counter

'''
how to use counter:
a=Counter('abcddeea')
print(a)
>> Counter({'a': 2, 'd': 2, 'e': 2, 'b': 1, 'c': 1})
print(a['a'])
>> 2
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        hash,5min
        '''
        arr = [0]*26
        for char in magazine:
            idx = ord(char)-97
            arr[idx] += 1
        for char in ransomNote:
            idx = ord(char)-97
            arr[idx] -= 1
            if arr[idx] < 0:
                return False
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        8min, counter
        '''
        m = Counter(magazine)
        r = Counter(ransomNote)
        return len(r-m) < 1

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''simplify the hashtable version'''
        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True
