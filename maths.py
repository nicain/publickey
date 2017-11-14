import math
import random
from fractions import gcd


def simple_is_prime(n):
    """ Simplest possible prime check.
        Returns True if n is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        # only need to check up to the sqrt of N
        if n % i == 0:
            return False
    return True

def prime_sieve(size):
    """ Sieve of Eratosthenes. Gives all primes less than `size'.
    """
    sieve = [True] * size
    sieve[0:2] = [False, False]
    
    for i in range(2, int(math.sqrt(size)) + 1):
        pointer = i * 2
        while pointer < size:
            sieve[pointer] = False
            pointer += i

    return [i for i in range(size) if sieve[i]]

def rabin_miller(n, k=5):
    """ Rabin-Miller prime testing algorithm.
    see: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """
    d = n-1
    r = 0
    while d % 2 == 0:
        d = d // 2
        r +=1

    # witness loop
    for attempts in range(k):
        a = random.randrange(2, n-1)
        x = pow(a, d, n)
        if x != 1:
            i = 0
            while x != (n-1):
                if i == (r-1):
                    return False
                else:
                    i = i + 1
                    x = (x ** 2) % n
    return True

def is_prime(n):
    """ Fancy prime test that first checks low primes, then uses
        Rabin-Miller.
    """
    if n < 2:
        return False

    low_primes = prime_sieve(1000)

    if n in low_primes:
        return True

    for prime in low_primes:
        if n % prime == 0:
            return False

    return rabin_miller(n)

def find_random_prime(start, stop):
    """ Finds a random prime within specified range.
    """
    while True:
        n = random.randrange(start, stop)
        if is_prime(n):
            return n

def find_random_coprime(n, start, stop):
    """ Finds a random number in the specified range that
        is coprime with n
    """
    while True:
        e = find_random_prime(start, stop)
        if gcd(e, n) == 1:
            return e

def multinv(mod, val):
    """ Multiplicative inverse of a value with a given modulus.

        that is, an integer x such that ax is congruent to 1 modulo M

        Does this require mod and val to be coprime?

        >>> multinv(11, 3)
        4 
        >>> (4 * 3) % 11
        1
    """
    # stolen from https://stackoverflow.com/questions/8539441/private-public-encryption-in-python-with-standard-library
    x, lastx = 0, 1
    a, b = mod, val
    while b:
        a, q, b = b, a // b, a % b
        x, lastx = lastx - q * x, x
    result = (1 - lastx * mod) // val
    return result + mod if result < 0 else result


def main():
    known_prime = 109182490673
    assert simple_is_prime(known_prime)
    assert rabin_miller(known_prime)
    assert is_prime(known_prime)
    

if __name__ == '__main__':
    main()