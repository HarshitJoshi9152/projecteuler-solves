from functools import reduce
"""
def factors(n):    
 return len(set(reduce(list.__add__, 
             ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
"""

"""
def factors(n):
    f = set([1, n]) if not n == 1 else set([1]) # maybe just start the loop from one
    for i in range(2, (n//2) + 1):
        # maybe we could optimise this more ?
        if not i in f and n % i == 0:
            f.update([i, n // i])
    return len(f)
"""

def factors(n):
    # f = set([1, n]) if not n == 1 else set([1]) # maybe just start the loop from one
    count = 0
    n_map = {}
    for i in range(1, int(n**0.5) + 1):
        # maybe we could optimise this more ?
        if n % i == 0 and not n_map.get(i, False):
            # we will store i not as property name by as value
            count += 2
            n_map[n//i] = i         # to avoid double counting
    return count

    #    if not i in f and n % i == 0:
    #        f.update([i, n // i])
    #return len(f)

if __name__ == "__main__":
    for i in range(1, 1000):
        factors(i)

"""
for StackOverflow factors function

real    0m0.031s
user    0m0.030s
sys     0m0.000s

My function

real    0m0.059s
user    0m0.058s
sys     0m0.000s

Updated function

real    0m0.035s
user    0m0.022s
sys     0m0.013s

"""
