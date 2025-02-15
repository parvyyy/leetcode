# 14/2/25
# https://leetcode.com/problems/product-of-the-last-k-numbers/description/

from functools import reduce
class ProductOfNums:
  def __init__(self):
    self.running_prod = [1]
    self.sz = 0

  def add(self, num: int) -> None:
    last = self.running_prod[self.sz]

    # Reset, as all future values will be dominated by the '0'.
    if num == 0:
      self.running_prod = [1]
      self.sz = 0

      return

    self.running_prod.append(last * num)
    self.sz += 1

  def getProduct(self, k: int) -> int:
    if k > self.sz:
      return 0

    prod = self.running_prod[self.sz] // self.running_prod[self.sz - k]

    return prod


p = ProductOfNums();
p.add(3);        # [3]
p.add(0);        # [3,0]
p.add(2);        # [3,0,2]
p.add(5);        # [3,0,2,5]
p.add(4);        # [3,0,2,5,4]
p.getProduct(2); # return 20. The product of the last 2 numbers is 5 * 4 = 20
p.getProduct(3); # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
p.getProduct(4); # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
p.add(8);        # [3,0,2,5,4,8]
p.getProduct(2); # return 32. The product of the last 2 numbers is 4 * 8 = 32
