from typing import List

"""
To carry the heaviest object, the capacity must be at LEAST
that weight. It must be at MOST the sum of all the weights,
and this would allow it to carry all the packages.

If a weight capacity w is not suitable, then any lower capacity
is not suitable. If a weight capacity is suitable, there MAY be 
a lower capacity that is also suitable. This monotonic behaviour 
allows us to use a binary search.

The 'hi' result is always a suitable weight capacity.
The 'lo' result is always NOT a suitable weight capacity
    - except for the initial
    - NOTE: This was true but the condition @ the start was not
            all inclusive, hence the final iteration was required.


"""
def shipWithinDays(weights: List[int], days: int) -> int:
    lo, hi = max(weights), sum(weights)

    def getNumDays(weights: List[int], capacity: int) -> int:
        ndays = idx = 0

        curr_total = 0
        while idx < len(weights):
            curr_total += weights[idx]

            if curr_total > capacity:
                ndays += 1
                curr_total = weights[idx]

            idx += 1

        return ndays + int(curr_total > 0)

    # Determines if the initial 'lo' is suitable.
    # Each package can be taken on its own day
    # and still meet the timing threshold.
    if days >= getNumDays(weights, lo):
        return lo

    while lo + 1 < hi:
        # Represents the current weight capacity
        mid = int((lo + hi) / 2)

        ndays = getNumDays(weights, mid)
        # print(lo, hi, mid, ndays)

        if ndays > days:
            lo = mid
        else:
            hi = mid

    return hi

res = shipWithinDays([2,4,6,1,3,10], 4)
print(res)

res = shipWithinDays([1,2,3,4,5], 5)
print(res)

res = shipWithinDays([1,5,4,4,2,3], 3)
print(res)