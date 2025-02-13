# 13/2/25
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/

import heapq

def minOperations(nums: list[int], k: int) -> int:
  heapq.heapify(nums)

  min_ops = 0
  while len(nums) > 1 and nums[0] < k:

    x, y = heapq.heappop(nums), heapq.heappop(nums)

    # Unnecessary to apply min & max as 'x' will always be the min of the two &
    # vice-versa.
    v = x * 2 + y
    heapq.heappush(nums, v)

    min_ops += 1

  return min_ops

print(minOperations([2,11,10,1,3], 10))
print(minOperations([1,1,2,4,9], 20))