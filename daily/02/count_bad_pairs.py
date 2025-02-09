# 9/1/25
# https://leetcode.com/problems/count-number-of-bad-pairs/description/

from math import comb
from collections import Counter

def countBadPairsNaive(nums: list[int]) -> int:
    n, bad_pair_count = len(nums), 0

    for i in range(n):
        for j in range(i + 1, n):
            if (j - i) != nums[j] - nums[i]:
                bad_pair_count += 1

    return bad_pair_count

def countBadPairs(nums: list[int]) -> int:
    n =  len(nums)

    # Note that (j - i) != nums[j] - nums[i] may be re-arranged to
    # nums[i] - i != nums[j] - j
    total = comb(n, 2)

    # Finds nums[i] - i
    c = Counter([n - i for i, n in enumerate(nums)])

    # Now, there will be 'k' copies of 'nums[i] - i'. These
    # k elements will all be 'good pairs'. 
    for k, count in c.items():
        # nC2 ways to pair these 'k' good pairs.
        c[k] = comb(count, 2)

    good_pairs = sum(c.values())

    return total - good_pairs

print(countBadPairs([4, 1, 3, 3]))
print(countBadPairs([1, 2, 3, 4, 5]))