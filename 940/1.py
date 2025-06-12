class Solution:
    def distinctSubseqII(self, s: str) -> int:
        '''
        seems combination
        2*(2^(n-1)-1)+1 = 2^n - 1
        which means: 2*prev + 1 = current (when no duplication)
        'adoagtmxle'
        end with a: a ->total+=(0+1)
        end with d: ad, d ->total+=(1+1)
        end with o: ao,ado, do,o... ->total+=(3+1)
        end with a: aa, ada, da, aoa, adoa, doa, oa, a : one duplication total+=(8(<-total+1) - 1(<-the prev result of end with a)=7)
        every time total *2+1
        '''
        MOD = 10**9+7
        substr_at_char = [0]*26

        count = 0
        for i in range(len(s)):
            char_idx = ord(s[i])-97
            # new_substr_at_char = (count+1)
            diff = (count+1-substr_at_char[char_idx]+MOD) % MOD
            substr_at_char[char_idx] = (substr_at_char[char_idx]+diff) % MOD
            count = (count+diff) % MOD

        return (count+MOD) % MOD


t = 'abc'
t = 'aba'
r = Solution().distinctSubseqII(t)
print(r)
