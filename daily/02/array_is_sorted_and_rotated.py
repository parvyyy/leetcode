# 2/2/25
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

from itertools import groupby

### Optimisations
#   A more natural solution is noticing there must be ONLY one 'inversion',
#   where nums[i] > nums[i + 1]. Thus, we must simply count the # of inversions.

def check(nums: list[int]) -> bool:
    nums = [k for k,_ in groupby(nums)]

    # Reversal is required as we require the LAST positional index of the
    # smallest element.
    minIdx, _ = min(reversed(list(enumerate(nums))), key=lambda x: x[1])

    nums = nums[minIdx:] + nums[:minIdx]

    def isSorted(nums: list[int]):
        n = len(nums)

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return False
            
        return True
    
    return isSorted(nums)

def checkOptimised(nums: list[int]) -> bool:
    n = len(nums)

    numInversion = 0
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            numInversion += 1

    if nums[-1] > nums[0]:
        numInversion += 1

    return numInversion <= 1

print(check([3,4,5,1,2]))
print(check([2,1,3,4]))
print(check([1,2,3]))
print(check([6,10,6]))
print(check([7,9,1,1,1,3]))


