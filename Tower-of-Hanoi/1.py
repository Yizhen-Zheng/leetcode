from math import inf


def TowerOfHanoi(todo: int, origin: list[int], target: list[int], other: list[int]):
    '''
    todo: todo numbers
    A: from
    B: target
    C: other
    '''
    # nothing can be removed from origin
    if todo == 0:
        return
    TowerOfHanoi(todo=todo-1, origin=origin, target=other, other=target)
    # the move process
    print('from: ', origin)
    print('to: ', target)
    cur = origin.pop()
    print('moved elem: ', cur)
    target.append(cur)
    TowerOfHanoi(todo=todo-1, origin=other, target=target, other=origin)
    return


t = 3
A, B, C = ['origin']+[n for n in range(t, 0, -1)], ['target'], ['other']
r = TowerOfHanoi(3, origin=A, target=B, other=C)
