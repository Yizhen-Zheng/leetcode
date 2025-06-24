
import math


class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        prime number that < n
        return how many prime numbers less than n
        brute-force: check from range (2, n), each check takes O(n) so it's a O(n^2)
        sieve of Eratosthenes: O(n log log n)
        n: check the whole arr (True or False)
        using each prime to mark p*p+p, p*p+2p, ... as False is approximately n/p 
        tota operations to mark all non-prime: sum(n/2, n/3, n/5, n/7...)(up to n**(1/2))
        = n * (1/2 + 1/3 + 1/5...)
        = n * The sum of the reciprocals of all prime numbers which is log log n
        why log:
        e.g., 
        n=2, prime-need-to-check = 0
        n=4, prime-need-to-check = 1 (2)
        n=8, prime-need-to-check = 1 (2)
        n=16, prime-need-to-check = 2 (2,3)
        n=32, prime-need-to-check = 3 (2,3,5)
        n=64, prime-need-to-check = 3 (2,3,5,7)

        since marking False in is_prime only happens from (2, sqrt(n)+1), the total time will be 
        O(n + nloglogn) =>  O(nloglogn)

        other:
        Harmonic behaviour: 
        harmonic series: 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... = O(log n)
        by make this series less dense:
        1/2 + 1/4 + 1/6 + 1/8 + ... = (1/2)(1/1 + 1/2 + 1/3 + 1/4 + ...) ≈ (1/2) log n
        (1/2 of total reciprocals of natural numbers series)
        also, there are roughly n/log n primes up to n.
        so the density of prime number amount total numbers will be n / (n/log n) = 1/log n

        so the sum of reciprocals of of prime numbers will be 
        (1/log n ) * log n =>1
        but we'll get loglogn
        '''
        if n < 3:
            return 0
        is_prime = [True]*n
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
                # if i < math.sqrt(n)+1:  #no need to check this cuz while loop will break automatically
                j = i*i
                while j < n:
                    is_prime[j] = False
                    j += i
        print(is_prime)
        return count


t = 2
# t = 3
t = 3000
r = Solution().countPrimes(t)
print(r)
