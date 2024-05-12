from typing import List

def maxArea(height: List[int]) -> int:
  lo, hi = 0, len(height) - 1
  maxArea = 0

  while lo < hi:
    dist = hi - lo

    area = min(height[hi], height[lo]) * dist
    maxArea = max(maxArea, area)

    if height[hi] > height[lo]:
      lo += 1
    elif height[hi] < height[lo]:
      hi -= 1
    else:
      lo += 1
      hi -= 1

  return maxArea

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))