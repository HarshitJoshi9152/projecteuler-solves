#!/usr/bin/env python3

# four million => 4_000_000


mem = {
        1: 1,
        2: 1
}

def fib(n):
    cache = mem.get(n, False)
    if cache:
        return cache
    else:
        mem[n] = fib(n - 1) + fib(n - 2);
        return mem[n]

m = 0
i = 3
while True:
    m = fib(i)
    if m > 4_000_000:
        mem[i] = 0
        break
    i += 1

print(sum([i for i in mem.values() if i % 2 == 0]))

