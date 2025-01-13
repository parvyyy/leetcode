# 13/1/25
# https://leetcode.com/problems/minimum-length-of-string-after-operations/description/

from collections import Counter
def minimumLength(s: str) -> int:
    freq = Counter(s)

    def rmClosestRes(x: int) -> int:
        if x % 2 == 0:
            return 2
        
        return 1

    minLen = sum(map(lambda x: rmClosestRes(x), freq.values()))
    
    return minLen

print(minimumLength("abaacbcbb"))
print(minimumLength("aa"))