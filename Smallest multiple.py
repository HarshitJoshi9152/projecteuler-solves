"""
# HCF * LCM = product

import functools

numbers = (list(range(1, 21)))

# i could have just done 21!
mul = lambda x, y: x*y
product = functools.reduce(mul, numbers, 1)


common_factors = []

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

p_factors = []
def findPrimeFactors(n, k):
    for i in range(k, n):
        if n % i == 0:
            if isPrime(i):
                p_factors.append(i)
                return findPrimeFactors(n // i, i)
    p_factors.append(n)
    return len(p_factors)

l = []
for n in numbers:
    # find prime factors
    p_factors = []
    findPrimeFactors(n, 2)
    l.append(p_factors)

# compiling common factors

def mm(a, b):
    r = []
    for i in a:
        if i in b:
          r.append(i)
          a.pop(a.index(i))
          b.pop(b.index(i))
    return r

common_factors = functools.reduce(mm, l, [])

HCF = functools.reduce(mul, common_factors, 1)

print(product//HCF)

"""

# LCM --- DAMN this worked !

import functools

numbers = (list(range(1, 21)))

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 100) if isPrime(x)]

mul = lambda x, y: x*y

# trying the common division method
def findLCM(nList, primesIndex = 0, results = []):
    # print(f"LEVEL {len(results)} {nList} \t {results}")
    for i in nList:
        divisor = primes[primesIndex]
        if i % divisor == 0:
            # if any number can be divided by a number,
            # we divide all the go to next level,
            # store the divisor

            nList = [n//divisor if n % divisor == 0 else n for n in nList]
            results.append(divisor)

            return findLCM(nList, primesIndex, results)
    # if all numbers in nList are not 1 move to next prime !
    if not nList == [1 for i in nList]:
        return findLCM(nList, primesIndex + 1, results)
    
    # only do this if all numbers in nList are 1 !!
    # meaning we have the entire combined prime factrisation
    # [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]
    lcm = functools.reduce(mul, results, 1)
    return lcm;

print(findLCM(numbers))

# postid => 389973