"""
Equivalent to a 1D list with m * n elements.
Due to the time constraint, we cannot map it to this.


Perform binary search
lo = 0 (0, 0)
hi = 11 (3, 4)
mid = 5.5 -> 5 (2, 1)

lo = 5 (2, 1)
hi = 11 (3, 4)
mid = 8 (3, 1)

lo = 8 (3, 1)
hi = 11 (3, 4)
mid = 9 (3, 2)

lo = 8 (3, 1)
hi = 9 (3, 2)
mid = 8 (3, 1)

"""

from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    n, m  = len(matrix), len(matrix[0])
    
    def to2D(idx: int) -> tuple[int, int]:
        r = idx // m
        c = idx % m
        return r, c
    
    lo, hi = 0, (m * n - 1)

    while lo <= hi:
        mid = int((lo + hi) / 2)

        if mid == lo or mid == hi:
            return False

        r, c = to2D(mid)
        mid_v = matrix[r][c]

        print(">", mid_v, target)

        if mid_v == target:
            return True
        elif mid_v < target:
            lo = mid
        else:
            hi = mid

    return False

res1 = searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
# res2 = searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15)

print(res1)
