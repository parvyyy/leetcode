from typing import List

"""
piles = [1,4,3,2], h = 9
As h >= length
k = max(piles)
k = 2 -> 6 hours
k = 1 -> 10 hours

For k = 1:max
    if h' < h => return k

"""
import math

# Time Complexity O(log(max(n)) * n)

# Key Point: If a rate works, any larger rate also works.
#            This allows binary search to be suitable.
def minEatingSpeed(piles: List[int], h: int) -> int:
    lo, hi = 1, max(piles)

    if h >= sum(piles):
        return 1

    while lo + 1 < hi:
        # Represents the current eating-rate.
        mid = math.ceil((lo + hi) / 2)

        h_prime = 0
        for pile in piles:
            h_prime += math.ceil(pile / mid)

        if h_prime <= h:
            hi = mid
        else:
            lo = mid

    return hi

res = minEatingSpeed([1, 4, 3, 2], 9)
print(res)

res = minEatingSpeed([25,10,23,4], 4)
print(res)

res = minEatingSpeed([25], h = 1) # 25
print(res)

res = minEatingSpeed([25], h = 4) # 7
print(res)

res = minEatingSpeed([312884470], 968709470)
print(res)