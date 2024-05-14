import sys

# Wrong! Does not guarantee minimum sub-array, but rather the middle one.
def minSubArrayLenInitial(target, nums):
  '''
  Set the sliding window as the entire array & calculate sum
    
    If the target is greater than the sum, return 0
    If the target is less than the sum, remove the smaller value off the end.
      Decrease from the sum.
      Repeat until the target < sum

  Returns len(minArr)
  '''
  lo, hi = 0, len(nums) - 1
  total = sum(nums)

  if target > total:
    return 0
  
  while lo < hi:
    if total < target:
      return len(nums) + 1
    
    total -= min(nums[lo], nums[hi])

    if nums[lo] < nums[hi]:
      nums = nums[lo + 1:hi]
    else:
      nums = nums[lo: hi - 1]

  return 0

def minSubArrayLen(target, nums):
  # Expand the sliding window until the sum is greater than target. Store the length
  # Move sliding window to the right until the sum is lower than target.
  # Repeat the above two steps


  i, j, total = 0, 0, 0
  minLen = sys.maxsize

  while i < len(nums):
    total += nums[i]
    i += 1

    # This triggers when the sliding window is greater than the target
    while total >= target:
      # i - j represents the size of the current sub-array. Replace the min
      # if less than, otherwise skip
      minLen = min(minLen, i - j)
      total -= nums[j]
      j += 1

  if minLen is sys.maxsize:
    return 0

  return minLen

print(minSubArrayLen(7, [2,3,1,2,4,3]))