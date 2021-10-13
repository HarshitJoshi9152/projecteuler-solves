"""
Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors
of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) =
a, where a != b, then a and b are an amicable pair and each of a and b are
called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4,
5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors
of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the
amicable numbers under 10000.

"""

def get_factors(n):
    factors = set([1])
    for i in range(2, int(n**1/2) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return factors

def isAmicable(a):
    # the factors also contain the number itself so we have to adjust the value by subtracting itself
    b = sum(get_factors(a));
    f_b = sum(get_factors(b));
    if f_b == a and a != b:
        return True
    return False

print(isAmicable(1))

ns = 0
for n in range(0, 10000):
    if isAmicable(n):
        ns += n
print(ns)

# 40285 wrong
# 31626
