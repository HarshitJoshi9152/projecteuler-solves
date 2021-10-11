"""
Maximum path sum I
Problem 18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
37 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 4 82 47 65
19 1 23 75 3 34
88 2 77 73 7 63 67
99 65 4 28 6 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 4 68 89 53 67 30 73 16 69 87 40 31
4 62 98 27 23 9 70 98 73 93 38 53 60 4 23
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

https://projecteuler.net/problem=18
"""


tree = [
	[75],
	[95, 64],
	[17, 47, 82],
	[18, 35, 87, 10],
	[20, 4, 82, 47, 65],
	[19, 1, 23, 75, 3, 34],
	[88, 2, 77, 73, 7, 63, 67],
	[99, 65, 4, 28, 6, 16, 70, 92],
	[41, 41, 26, 56, 83, 40, 80, 70, 33],
	[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
	[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
	[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
	[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
	[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
	[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

# tree = [
# 	[3],
# 	[7, 4],
# 	[2, 4, 6],
# 	[8, 5, 9, 3]
# ]



def solve(lvl, index):
	# binary tree !
	if (lvl >= len(tree) or index >= len(tree[lvl]) or index < 0):
		return 0
	else:
		elm = tree[lvl][index]
		# print(f"{elm=}")
		left_sum = solve(lvl + 1, index - 1 + 1)
		# if left_sum != 0:
		# 	print(f"{left_sum=}")
		right_sum = solve(lvl + 1, index + 1 )
		# if left_sum != 0:
		# 	print(f"{right_sum=}")
		# print(elm + max(left_sum, right_sum))
		return elm + max(left_sum, right_sum)

print(solve(0, 0))

# 1016 first try WRONG
# 1074 second try after testing sample input
# 	logic was ok but the indexes for next nodes were wrongly computed

# You are the 146747th person to have solved this problem.!