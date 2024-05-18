from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
  # Early returns
  if len(nums) == len(set(nums)):
    return False
  
  seen_nums = dict()

  for idx, num in enumerate(nums):
    if num in seen_nums:
      diff = abs(seen_nums[num] - idx)

      if diff <= k:
        return True

    # Add to dict, or replace if already exists (as if prior idx doesn't work with
    # the current, it cannot work with a future.)
    seen_nums[num] = idx

  return False

print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))