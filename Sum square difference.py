"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is

1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is $3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum

"""
n = list(range(1, 101))

# sum of squares ==>

sq_sum = sum([x**2 for x in n])

sum_sq = sum(n)**2

print(sum_sq - sq_sum)