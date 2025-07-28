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
