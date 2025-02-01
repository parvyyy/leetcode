# 1/2/25
# https://leetcode.com/problems/special-array-i/description/

def isArraySpecial(nums: list[int]) -> bool:
    n = len(nums)

    if n == 0 or n == 1:
        return True
    
    for i in range(n - 1):
        if nums[i] % 2 == nums[i + 1] % 2:
            return False
        
    return True

print(isArraySpecial([1]))
print(isArraySpecial([2,1,4]))
print(isArraySpecial([4,3,1,6]))