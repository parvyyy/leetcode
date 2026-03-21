"""
Non-negative integer --> 1, 2, 3, ..., n
Do not have to worry about [0, 1]
The square root of a number must be smaller than it.
The square root must be less than half the number.
 - to always round down for non integer halves.

As this is a binary search question, we will capture
the middle element. Check the result when multiplied by itself.
If it is higher than x, set the element to the upper.
If it is lower than x, set the element to the lower.

[0, 13] m = 6
[0, 6] m = 3
[3, 6] m = 4
[3, 4] m = 3

When lo & hi have a difference of 1, we know to take the lower value.
Lower as the question states we want the rounded down result.
"""

def mySqrt(x: int) -> int:
    if x == 0 or x == 1 or x == 2:
        return x
    
    lo, hi = 0, x

    while lo + 1 < hi:
        mid = int((lo + hi) / 2)

        r = mid * mid

        if r == x:
            return mid
        
        if r > x:
            hi = mid
        else:
            lo = mid

    return lo

res = mySqrt(4)
print(res)