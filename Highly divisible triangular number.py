"""
Highly divisible triangular number
Problem 12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""

def factors(n):
    count = 0
    n_map = {}
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0 and not n_map.get(i, False):
            # we will store i not as property name by as value
            count += 2
            n_map[n//i] = i         # to avoid double counting
    return count

# starting from trian no 2 => 3
prev_triag_num = 3
n = 3

while True:
    elm = prev_triag_num + n
    f_len = factors(elm)
    if f_len > 500:
        print(elm)
        break
    prev_triag_num = elm
    n += 1

"""
➤ time python Highly\ divisible\ triangular\ number.py
76576500

________________________________________________________
Executed in    4.34 secs   fish           external 
   usr time    4.33 secs    0.00 micros    4.33 secs 
   sys time    0.00 secs  847.00 micros    0.00 secs 
"""