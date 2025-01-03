# https://leetcode.com/problems/number-of-ways-to-split-array/description/
# 3/1/25
""" 
Find the total sum of nums. Then, have a running total as nums is iterated through,
the sum of the first i + 1 elements is the running total, while the sum of the last
n - i - 1 is the difference between the total and running total.

If it is greater, add one to the split counter.
"""
def waysToSplitArray(nums: list[int]) -> int:
    total_sum, running_total = sum(nums), 0
    split_count = 0

    for (i, n) in enumerate(nums):
        if i == len(nums) - 1:
            break

        running_total += n
        diff = total_sum - running_total

        if running_total >= diff:
            split_count += 1

    return split_count

print(waysToSplitArray([10,4,-8,7])) # 2
print(waysToSplitArray([2,3,1,0])) # 2
