# 25/02/25
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/

def numOfSubarraysNaive(arr: list[int]) -> int:
    n = len(arr)
    
    total, i = 0, 0
    for i in range(n):
        local_sum = 0
        for j in range(i, n):
            local_sum += arr[j]

            if local_sum % 2 == 1:
                total += 1

    return total % (10 ** 9 + 7)

def numOfSubarraysOptimised(arr: list[int]) -> int:
    n = len(arr)
    
    numOdd = [0 for _ in range(n)]

    local_sum = count = 0
    for i in range(n):
        local_sum += arr[i]
        count += (local_sum % 2 == 1)

    numOdd[0] = count

    for j in range(1, n):
        isPrevEven = arr[j - 1] % 2 == 0

        if isPrevEven:
            numOdd[j] = numOdd[j - 1]
        else:
            numOdd[j] = (n - (j - 1)) - numOdd[j - 1]

        count += numOdd[j]

    return count % (10 ** 9 + 7)

def numOfSubarraysFurtherOptimised(arr: list[int]) -> int:
    summ = odd = even = 0
    for v in arr:
        summ += v

        if summ % 2:
            odd += 1
        else: 
            even += 1

    return odd * (even + 1) % (10 ** 9 + 7)

print(numOfSubarraysOptimised([1,2,3,4,5,6,7]))