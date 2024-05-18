from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  seen_numbers = dict()

  for idx, num in enumerate(nums):
    if target - num in seen_numbers:
      return [seen_numbers[target - num], idx]

    # Store the num as the key & it's idx as the val.
    seen_numbers[num] = idx


  return []


print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))