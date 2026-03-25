from typing import List

def findMin(nums: List[int]) -> int:
    n = len(nums)
    lo, hi = 0, n - 1

    while lo + 1 < hi:
        mid = int((lo + hi) / 2)
        print(lo, mid, hi)

        if nums[lo] < nums[mid]:
            if nums[lo] < nums[hi]:
                hi = mid
            else:
                lo = mid
        elif nums[hi] > nums[mid]:
            if nums[lo] < nums[hi]:
                lo = mid
            else:
                hi = mid

    return min(nums[lo], nums[hi])

res = findMin([3,4,5,6,1,2])
print(res)

res = findMin([4,5,0,1,2,3])
print(res)

res = findMin([4,5,6,7])
print(res)