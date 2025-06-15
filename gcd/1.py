'''

the Euclidean algorithm:
a=9, b=6: 9%6=3
a=6, b=3: 6%3==0, 3 is the gcd
proof gcd(a,b) == gcd(d,r):
    1:
    set cd to be a common divisor of a and b -> a = k*cd, b = l*cd
    a = b*q + r (q: quotient)
    a = k*cd = l*cd*q+r
    r = cd*(k - l*q), 
    therefore if a, b have a common divisor cd, then cd is also a common divisor of r
    2:
    conversely: 
    set cd to be a common divisor of b and r -> b = m*cd, r = n*cd
    a = b*q+r 
      = m*q*cd + n*cd 
      = (m*q + n)*cd
    therefore if b, r have a common divisor cd, then cd is also a common divisor of a

time complexity: O((log a)^3)

least common multiple:
lcm = a / cd * b
'''


def gcb(a, b):
    '''
    positive int, a > b
    can be write into recursion(return a if b==0 else gcb(b,a%b))
    '''
    # return a if b == 0 else gcb(b, a % b)
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


r = gcb(20, 50)
print(r)
