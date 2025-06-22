def binary_expo(a, b):
    '''
    calculate a^b
    a: base number; b: power 
    '''
    res = 1
    while b:
        if b & 1:
            res *= a
        a *= a
        b = b >> 1
        # prepare a for next digit
        # (16, 8, 4, 2, 1)
        # (1   1  0  0  0) -> 12
        # if current digit is 1, add this digit to result, else, skip this digit
        # it's like DP, the next step is using it's prev's result(digit 4 is using digit 2^2, so on)
    return res


t = binary_expo(2, 12)
print(t)
