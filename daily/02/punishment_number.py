# 15/2/25
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

from itertools import permutations
def punishment_number(n: int):
    punishment_number = 0

    def isPartitionable(s: str, target: int) -> bool:
        if s == "" and target == 0:
            return True
        
        if target < 0:
            return False
        
        n_digits = len(s)

        for i in range(n_digits):
            # We will keep the LHS & recurse on the RHS.
            l, r = s[:i+1], s[i+1:]

            isPossible = isPartitionable(r, target - int(l))

            if isPossible:
                return True

        return False

    for i in range(1, n + 1):
        s = str(i * i)
        if isPartitionable(s, i):
            punishment_number += i * i

    return punishment_number


print(punishment_number(10))