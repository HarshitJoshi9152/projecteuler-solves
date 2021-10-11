"""
Lattice paths
Problem 15

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

"""

# classic grid traveller problem

map_ = {}

def findPaths(r, c):
    if r == 0 and c == 0:
        return 1
    elif r < 0 or c < 0:
        # wrong path couldnt end up on the ending coordinate
        return 0
    p_c = map_.get(str([r,c]), False)
    if p_c:
        return p_c
    paths = findPaths(r - 1, c) + findPaths(r, c - 1) 
    map_[str([r,c])] = paths
    return paths

print(findPaths(20, 20))
