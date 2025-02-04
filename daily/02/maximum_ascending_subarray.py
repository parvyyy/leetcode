# 4/1/25
# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/

def maxAscendingSum(nums: list[int]) -> int:
    # Sliding window approach
    n = len(nums)

    if n == 1:
        return nums[0]
    
    i, j = 0, 1

    maxx = 0
    for i in range(n):
        # Move i to the end of the current window.
        if i != j - 1:
            continue
        
        local_maxx = nums[i]

        while j < n and nums[j] > nums[j - 1]:
            local_maxx += nums[j]
            j += 1

        # Start j at next element after the end of the curr window.
        j += 1

        maxx = max(maxx, local_maxx)

    return maxx

print(maxAscendingSum([1]))
print(maxAscendingSum([10, 20, 30, 5, 10, 50]))
print(maxAscendingSum([10, 20, 30, 5]))
print(maxAscendingSum([10, 20, 30]))
print(maxAscendingSum([12, 17, 15, 13, 10, 11, 12]))
print(maxAscendingSum([10, 20, 30, 40, 50]))
print(maxAscendingSum([3, 6, 10, 1, 8, 9, 9, 8, 9]))
