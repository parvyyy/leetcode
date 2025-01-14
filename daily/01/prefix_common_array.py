# 14/1/25
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/

"""
    Two pass method:
    Go through zip(a, b), adding elements of A to a set. Use an array, acting as a prefix sum
    adding onto it if the element at B is in the set.

    [0, 1, 2, 3]

    Perform the same but this time adding elements of B to the set.

    [0, 1, 2, 3]


    Add the two resultant prefix sums as follows.
    * If A[i] != B[i], sum the ith index of each. Add 1 to a tracker.
    * Otherwise, simply add the tracker to one of them (they should both be the same)

    [0, 0, 1]
    [0, 1, 1]
    [0, 1, 2 + 1], tracker = 1

    The above did NOT work -- using multiple prefix-sums often leads to double counting and having to
    deal with several edge cases. Keep it simple :)
"""

from typing import List

def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    # Create a binary array storing if the ith element of B has appeared in A[:i]
    comm_A, pref_set = [0] * len(A), set()
    for i in range(len(A)):
        pref_set.add(A[i])
        comm_A[i] = int(B[i] in pref_set)
    
    # Create a binary array storing if the ith element of A has appeared in B[:i]
    comm_B, pref_set = [0] * len(B), set()
    for i in range(len(B)):
        pref_set.add(B[i])
        comm_B[i] = int(A[i] in pref_set)

    # The idea is that either the prefix_common_array increases by 0, 1 or 2.
    # That is, we may add comm_A[i] & comm_B[i], as they independantly track the commonality
    # btwn the two lists.
    
    # An additional consideration is that if A[i] and B[i] were the same, the commonality
    # has been double counted, appearing in both comm_A and comm_B. This is fixed using the
    # 'offset'.

    prefix_common = [0] * len(A)
    for i in range(len(A)):
        offset = comm_A[i] + comm_B[i]

        if A[i] == B[i]:
            offset -= 1

        # Handles first case, where element i - 1 does not exist
        if i == 0:
            prefix_common[i] = 0 + offset
            continue
        
        prefix_common[i] = prefix_common[i - 1] + offset
    
    return prefix_common

print(findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]))
print(findThePrefixCommonArray([1, 2, 3], [1, 3, 2]))
print(findThePrefixCommonArray([2, 3, 1], [3, 1, 2]))
print(findThePrefixCommonArray([1], [1]))