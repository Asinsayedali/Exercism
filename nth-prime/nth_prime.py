import math


def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    num = 2
    primes = []
    while len(primes) < number:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes[-1]


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True
