# 12/02/25
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description

from collections import defaultdict
from functools import reduce

class BigTwo:
  def __init__(self):
    self.large = -1
    self.larger = -1

  def add(self, n: int) -> None:
    # No change, there is no difference to the biggest two
    if n <= self.large:
      return

    # Replace 'large' with 'n'
    if n <= self.larger:
      self.large = n
      return

    # Replace 'large' with 'larger' & 'larger' with 'n'.
    self.large = self.larger
    self.larger = n

    return

  def sum(self) -> int:
    if self.large == -1 or self.larger == -1:
      return -1

    return self.large + self.larger

  def __str__(self):
    return f"L: {self.larger}, l: {self.large}"

def maximumSum(nums: list[int]) -> int:
  max_per_digit = defaultdict(lambda: BigTwo())

  for num in nums:
    digit_sum = reduce(lambda x, y: int(x) + int(y), str(num))

    # Unknown why this breaks -- most likely a quirk with '0'
    digit_sum = int(digit_sum)

    max_per_digit[digit_sum].add(num)

  maxx = -1
  for (_, bt) in max_per_digit.items():
    maxx = max(maxx, bt.sum())

  return maxx

print(maximumSum([1,9,1,3,10]))
# print(maximumSum([18,43,36,13,7]))
# print(maximumSum([10,12,19,14]))
# print(maximumSum([18,43,36,36,13,7]))