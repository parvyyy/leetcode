# 6/2/25
# https://leetcode.com/problems/tuple-with-same-product/description/

from collections import defaultdict
from math import comb

def tupleSameProduct(nums: list[int]) -> int:
    n = len(nums)

    products = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if j <= i:
                continue
            
            product = nums[i] * nums[j]
            products[product] += 1

    count = 0
    for num_prod in products.values():
        # Number of ways to pick two tuples.
        p = comb(num_prod, 2)

        # For a tuple pair (a, b) there are 2! ways to arrange the elements within.
        # For a pair of tuples, there are 2! ways to arrange them.
        # Hence, the # of ways to arrange 2-tuples into a 4-tuple is 2 * 2 * 2 = 8.
        count += 8 * p

    return count

print(tupleSameProduct([2,3,4,6]))
print(tupleSameProduct([1,2,4,5,10]))


