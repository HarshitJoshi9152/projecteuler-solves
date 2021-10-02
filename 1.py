import sys

l = 1000 if len(sys.argv) < 2 else int(sys.argv[1])
s = 0
for i in range(l):
    if i % 3 == 0:
        s += i
    elif i % 5 == 0:
        s += i
print(s)
