'''
Sort the stack in ascending order (smallest element at the bottom and largest at the top).
t: n**2
s: n
'''


def SortStackWithRecursion(stack: list[int]):
    def rec(s: list[int]):
        if not s:
            return
        elem = s.pop()
        rec(s)
        insert(s, elem)
    rec(stack)
    return stack


def insert(s: list[int], elem: int):
    '''given a sorted s, insert'''
    if not s or s[-1] < elem:
        s.append(elem)
        return
    cur_num = s.pop()
    insert(s, elem)
    s.append(cur_num)


t = [1, 2, 3]
t = [3, 2, 1]
t = [41, 3, 32, 2, 11]
r = SortStackWithRecursion(t)
print(r)
