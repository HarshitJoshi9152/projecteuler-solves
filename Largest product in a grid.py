"""
Largest product in a grid
Problem 11

In the 20x20 grid "below", four numbers along a diagonal line have been marked in "red"

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 x 63 x 78 x 14 = 1788696.
What is the greatest product of four adjacent numbers in the same direction
("up", "down", "left", "right", or diagonally) in the 20x20 "grid"?,
"""


import numpy as np
from functools import reduce

block = [
    ["08", "02", "22", "97", "38", "15", "00", "40", "00", "75", "04", "05", "07", "78", "52", "12", "50", "77", "91", "08"],
    ["49", "49", "99", "40", "17", "81", "18", "57", "60", "87", "17", "40", "98", "43", "69", "48", "04", "56", "62", "00"],
    ["81", "49", "31", "73", "55", "79", "14", "29", "93", "71", "40", "67", "53", "88", "30", "03", "49", "13", "36", "65"],
    ["52", "70", "95", "23", "04", "60", "11", "42", "69", "24", "68", "56", "01", "32", "56", "71", "37", "02", "36", "91"],
    ["22", "31", "16", "71", "51", "67", "63", "89", "41", "92", "36", "54", "22", "40", "40", "28", "66", "33", "13", "80"],
    ["24", "47", "32", "60", "99", "03", "45", "02", "44", "75", "33", "53", "78", "36", "84", "20", "35", "17", "12", "50"],
    ["32", "98", "81", "28", "64", "23", "67", "10", "26", "38", "40", "67", "59", "54", "70", "66", "18", "38", "64", "70"],
    ["67", "26", "20", "68", "02", "62", "12", "20", "95", "63", "94", "39", "63", "08", "40", "91", "66", "49", "94", "21"],
    ["24", "55", "58", "05", "66", "73", "99", "26", "97", "17", "78", "78", "96", "83", "14", "88", "34", "89", "63", "72"],
    ["21", "36", "23", "09", "75", "00", "76", "44", "20", "45", "35", "14", "00", "61", "33", "97", "34", "31", "33", "95"],
    ["78", "17", "53", "28", "22", "75", "31", "67", "15", "94", "03", "80", "04", "62", "16", "14", "09", "53", "56", "92"],
    ["16", "39", "05", "42", "96", "35", "31", "47", "55", "58", "88", "24", "00", "17", "54", "24", "36", "29", "85", "57"],
    ["86", "56", "00", "48", "35", "71", "89", "07", "05", "44", "44", "37", "44", "60", "21", "58", "51", "54", "17", "58"],
    ["19", "80", "81", "68", "05", "94", "47", "69", "28", "73", "92", "13", "86", "52", "17", "77", "04", "89", "55", "40"],
    ["04", "52", "08", "83", "97", "35", "99", "16", "07", "97", "57", "32", "16", "26", "26", "79", "33", "27", "98", "66"],
    ["88", "36", "68", "87", "57", "62", "20", "72", "03", "46", "33", "67", "46", "55", "12", "32", "63", "93", "53", "69"],
    ["04", "42", "16", "73", "38", "25", "39", "11", "24", "94", "72", "18", "08", "46", "29", "32", "40", "62", "76", "36"],
    ["20", "69", "36", "41", "72", "30", "23", "88", "34", "62", "99", "69", "82", "67", "59", "85", "74", "04", "36", "16"],
    ["20", "73", "35", "29", "78", "31", "90", "01", "74", "31", "49", "71", "48", "86", "81", "16", "23", "57", "05", "54"],
    ["01", "70", "54", "71", "83", "51", "54", "69", "16", "92", "33", "48", "61", "43", "52", "01", "89", "19", "67", "48"]
]

num_block = list(map(lambda i: list(map(int, i)), block))
"""
class Buffer:
    def __init__(self, max_len):
        self.stack = []
        self.MAX_LEN = max_len
        self.max_sum = 0
        self.result_stack = []

    def update(self, val):
        self.stack.append(val)
        if len(self.stack) > self.MAX_LEN:
            self.stack.pop(0)
            s = self.sum()
            if self.max_sum < s:
                if not 0 in self.stack:
                    self.max_sum = s
                    self.result_stack = self.stack.copy()

    def sum(self):
        return sum(self.stack)

    def clear(self):
        self.stack = []

    def __repr__(self):
        if len(self.stack) == self.MAX_LEN:
            return str(self.stack) + " = " + str(reduce(lambda x, y: x * y, self.stack, 1))
        else:
            return ""

# now the same buffer can be used to loop over all the directions
# we just need to transformm the matrix.
# hmm try later
"""


def out_of_bounds(r, c, matrix):
        if r >= len(matrix) or r < 0:
            return True
        if c >= len(matrix[0]) or c < 0:
            return True
        return False

def solve2():
    matrix = np.array(num_block)

    def element_product(r, c):
        seq = []
        product = 0
    
        # down
        p = 1
        s = []
        for r_i in range(r, r + 4):
            if out_of_bounds(r_i, c, matrix):
                break
            p *= matrix[r_i][c]
            s.append([r_i, c])
        print(s, p, "# down")
        if p > product:
            product = p
            seq = s.copy()
        
        # up
        p = 1
        s = []
        for r_i in range(r - 3, r + 1):
            if out_of_bounds(r_i, c, matrix):
                break
            p *= matrix[r_i][c]
            s.append([r_i, c])
        print(s, p, "# up")
        if p > product:
            product = p
            seq = s.copy()
        
        # right
        p = 1
        s = []
        for c_i in range(c, c + 4):
            if out_of_bounds(r, c_i, matrix):
                break
            p *= matrix[r][c_i]
            s.append([r, c_i])
        print(s, p, "# right")
        if p > product:
            product = p
            seq = s.copy()
        
        # left
        p = 1
        s = []
        for c_i in range(c - 3, c + 1):
            if out_of_bounds(r, c_i, matrix):
                break
            p *= matrix[r][c_i]
            s.append([r, c_i])
        print(s, p, "# left")
        if p > product:
            product = p
            seq = s.copy()
        
        # down-right
        s = []
        p = 1
        for r_i, c_i in zip(range(r, r + 4), range(c, c + 4)):
            if out_of_bounds(r_i, c_i, matrix):
                break
            p *= matrix[r_i][c_i]
            s.append([r_i, c_i])
        print(s, p, "down-right")
        if p > product:
            product = p
            seq = s.copy()
        
        # up-right
        p = 1
        s = []
        for r_i, c_i in zip(range(r - 3, r + 1), reversed(range(c, c+4))):
            if out_of_bounds(r_i, c_i, matrix):
                break
            p *= matrix[r_i][c_i]
            s.append([r_i, c_i])
        print(s, p, "up-right")
        if p > product:
            product = p
            seq = s.copy()
        
        # down-left
        p = 1
        s = []
        for r_i, c_i in zip(range(r, r + 4), reversed(range(c-3, c+1))):
            if out_of_bounds(r_i, c_i, matrix):
                break
            p *= matrix[r_i][c_i]
            s.append([r_i, c_i])
        print(s, p, "down-left")
        if p > product:
            product = p
            seq = s.copy()
        
        # up-left
        p = 1
        s = []
        for r_i, c_i in zip(range(r - 3, r + 1), range(c-3, c+1)):
            if out_of_bounds(r_i, c_i, matrix):
                break
            p *= matrix[r_i][c_i]
            s.append([r_i, c_i])
        print(s, p, "up-left")
        if p > product:
            product = p
            seq = s.copy()

        return (product, seq)

    max_prod = 1
    for r,_ in enumerate(matrix):
        for c,_ in enumerate(_):
            print(f"row = {r}, col = {c}")
            p, seq = element_product(r, c)
            if max_prod < p:
                max_prod = p
                print("MAD MAX !")
                print(str(seq).ljust(50), list(map(lambda x: matrix[x[0]][x[1]], seq)))

    print(max_prod)

solve2()
