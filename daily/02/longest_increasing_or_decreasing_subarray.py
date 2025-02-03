# 3/1/25
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/

def longestMonotonicSubarray(nums: list[int]) -> int:
    n = len(nums)

    if n == 0:
        return 0

    lsi = inc = 1
    for i in range(n - 1):
        if nums[i + 1] > nums[i]:
            inc += 1
        else:
            inc = 1

        lsi = max(lsi, inc)

    lsd = dec = 1
    for i in range(n - 1):
        if nums[i + 1] < nums[i]:
            dec += 1
        else:
            dec = 1

        lsd = max(lsd, dec)

    return max(lsi, lsd)

print(longestMonotonicSubarray([1,4,3,3,2]))
print(longestMonotonicSubarray([3,3,3,3]))
print(longestMonotonicSubarray([3,2,1]))