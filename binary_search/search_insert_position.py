from typing import List

def searchInsert(nums: List[int], target: int) -> int:
  # Iterative Binary Search
  lo, hi = 0, len(nums) - 1

  while lo < hi:
    mid = (lo + hi) // 2

    if nums[mid] == target:
      return mid
    
    if nums[mid] < target:
      lo = mid + 1

    if nums[mid] > target:
      hi = mid - 1

  return lo if nums[lo] >= target else lo + 1

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3,5,6], 0))
