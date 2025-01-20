# 20/1/25
# https://leetcode.com/problems/first-completely-painted-row-or-column/

from collections import defaultdict
"""
    Store the n_r, n_c.

    Create a dictionary, mapping the value in the matrix to its (r,c) index. [O(mn)]
    Create a dictionary for the rows & columns

    Iterate through arr, find (r,c) for the given value. Add 1 to row[r] & col[c].

    At each iteration, go through rows & cols & do checks! (O(m + n)) * O(mn).
    Instead, just check row[r] & col[c]!
"""

def firstCompleteIndex(arr: list[int], mat: list[list[int]]) -> int:
    m, n = len(mat), len(mat[0])

    mat_to_idx = dict()
    for (r, row) in enumerate(mat):
        for (c, cell) in enumerate(row):
            mat_to_idx[cell] = (r, c)

    # When mapping idx to a counter, we may use a list rather than a
    # dict / defaultdict!
    rows, cols = [0] * m, [0] * n

    for (i, v) in enumerate(arr):
        (r, c) = mat_to_idx[v]

        rows[r] += 1
        cols[c] += 1

        if rows[r] == n or cols[c] == m:
            return i

    return -1

print(firstCompleteIndex([1], [[1]]))
print(firstCompleteIndex([1,4,5,2,6,3], [[4,3,5],[1,2,6]]))
print(firstCompleteIndex([1,3,4,2], [[1,4],[2,3]]))
print(firstCompleteIndex([2,8,7,4,1,3,5,6,9], [[3,2,5],[1,4,6],[8,7,9]]))


