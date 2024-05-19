from typing import List
from collections import defaultdict

def longestConsecutive(nums: List[int]) -> int:
  num_tracker = dict()

  for num in nums:
    num_tracker[num] = False

  maxLen = 0

  for num in num_tracker.keys():
    # If the prev key has already been visited, then the current number must have been part of an earlier sequence.
    # That sequence will always have a longer length.

    # NOTE: Timeout Exceeded for checking if num_tracker[num] is True (i.e, visited). 

    if num - 1 in num_tracker:
      continue

    loc_max = 0

    while num in num_tracker:
      # Mark as visited
      num_tracker[num] = True

      loc_max += 1
      num += 1
    
    maxLen = max(maxLen, loc_max)

  return maxLen


print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))