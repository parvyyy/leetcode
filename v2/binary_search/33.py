from typing import List

def search(nums: List[int], target: int) -> int:
    n = len(nums)
    lo, hi = 0, n - 1

    if nums[lo] == target:
        return lo
    
    if nums[hi] == target:
        return hi

    while lo + 1 < hi:
        mid = int((lo + hi) / 2)

        if nums[mid] == target:
            return mid
        
        # NOTE: We do not need to check for
        #       equality as 'hi' & 'lo' have
        #       been set as a prev. 'mid' which
        #       has been checked for equality.

        # That [mid, hi] is SORTED
        if nums[mid] < nums[hi]:
            if nums[mid] < target < nums[hi]:
                lo = mid
            else:
                hi = mid

        # That [lo, mid] is SORTED
        else:
            if nums[lo] < target < nums[mid]:
                hi = mid
            else:
                lo = mid

    return -1

print(search([3,4,5,6,1,2], 1))
print(search([3,5,6,0,1,2], 4))