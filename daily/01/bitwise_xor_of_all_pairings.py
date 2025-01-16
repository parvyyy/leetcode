# 16/1/25
# https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/

from functools import reduce

"""
    The naive solution is create nums3 -- containing the XOR of all pairings.
    nums3 = [2,5,1,6]

    This can be expanded to be
    nums3 = [ 1 ^ 3, 1 ^ 4, 2 ^ 3, 2 ^ 4 ]

    Note that x ^ y is the same as y ^ x.

    Then the final answer will be:
    = 1 ^ 3 ^ 1 ^ 4 ^ 2 ^ 3 ^ 2 ^ 4
    = 1 ^ 1 ^ 2 ^ 2 ^ 3 ^ 3 ^ 4 ^ 4
    = 0 ^ 0 ^ 0 ^ 0 [computed in pairs]
    = 0

    That is n ^ n ^ .. ^ n = 0 if there are an even number & n if odd.

    Hence, given nums1 & nums2, if nums1 has an even amount of elements,
    there will be an even amount of XOR operations for all elements in num2.
    Hence the resultant XOR will be 0. This applies vice versa.

    Otherwise, if there is an odd number of elements, the resultant XOR will be
    the XOR of all elements.
"""

# O(m + n)
def xorAllNums(nums1: list[int], nums2: list[int]) -> int:
    m, n = len(nums1), len(nums2)

    if m % 2 == n % 2 == 0:
        return 0
    
    xor = 0
    
    # Each element in nums1 will be XOR'd an odd number of times with itself [leading
    # to itself -- as x ^ x ^ x == x] before being XOR'd with one another.
    if n % 2 != 0:
        xor ^= reduce(lambda x, y: x ^ y, nums1)
    
    # Similarly, as above.
    if m % 2 != 0:
        xor ^= reduce(lambda x, y: x ^ y, nums2)
    
    return xor

print(xorAllNums([2,1,3], [10,2,5,0]))
print(xorAllNums([1, 2], [3, 4]))