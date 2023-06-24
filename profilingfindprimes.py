import random

def guess():
    return random.randint(2, 5000)

def isPrime(x):
    for i in range(x):
        for j in range(x):
            if i * j == x:
                return False
    return True

def findPrimes(num):
    primes = []
    for i in range(num):
        p = guess()
        if isPrime(p):
            primes += [p]
    return primes

import cProfile
cProfile.run('print(findPrimes(500)[:10])')
