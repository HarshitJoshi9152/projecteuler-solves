"""
Longest Collatz sequence

Problem 14

The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""


chains_map = {
        # int: length
}

def collatz(n):
    # querying cache
    cache = chains_map.get(n, False)
    if cache:
        return cache
    # ending base case
    if n <= 1:
        return len([n])
    # main recursion code !
    next_n = n // 2 if n % 2 == 0 else n * 3 + 1
    #print(str(n) + " -> " + str(next_n) + " ", end="\t")
    steps = collatz(next_n) # steps is `int len
    chains_map[n] = 1 + steps
    return chains_map[n]

max_l = 0
max_i = 0
for i in range(1, 1_000_001):
    l = collatz(i);
    #print(f"{i}={l}")
    if l > max_l:
        max_l = l
        max_i = i

print(f"{max_l=}")
print(f"{max_i=}")

"""

max_l=525
max_i=837799

real    0m2.898s
user    0m2.763s
sys     0m0.125s

"""
