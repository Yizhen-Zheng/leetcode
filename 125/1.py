
class Solution:
    '''6min + debug 6min'''

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            cl, cr = s[l].lower(), s[r].lower()

            if (cl.isalpha() or cl.isdigit()) and (cr.isalpha() or cr.isdigit()):
                if cl != cr:
                    return False
                l += 1
                r -= 1
            elif not (cl.isalpha() or cl.isdigit()):
                l += 1
            elif not (cr.isalpha() or cr.isdigit()):
                r -= 1
        return True
