def ReverseStackWithRecursion(stack: list[int]):
    '''
    solution
    1, memo top elem, then insert to bottom
    '''
    def dfs(s: list[int]):
        if not s:
            return s
        num = s.pop()
        dfs(s)
        insert(s, num)

    def insert(s: list[int], elem: int):
        if not s:
            s.append(elem)
            return s
        memo = s.pop()
        insert(s, elem)
        s.append(memo)
    dfs(stack)

    return stack


def ReverseStackWithRecursion(stack: list[int]):
    '''
    solution
    2, memo bottom elem, then push to top
    '''
    def dfs(s: list[int]):
        if not s:
            return s
        bottom_elem = pool(s)
        dfs(s)
        s.append(bottom_elem)

    def pool(s: list[int]):  # only remove the bottom elem, push all rest elems back
        memo = s.pop()
        if not s:
            return memo
        bottom_elem = pool(s)
        s.append(memo)
        return bottom_elem

    dfs(stack)
    return stack


'''
t: n**2
s: n
'''
t = [1, 2, 3, 4]
r = ReverseStackWithRecursion(t)
print(r)
