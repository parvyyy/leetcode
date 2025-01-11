# 11/1/25
# https://leetcode.com/problems/construct-k-palindrome-strings/

from collections import Counter
"""
    We are required to split the string 's' into 'k' sections -- each of
    which is a palindrome.

    A palindrome must have each character appear twice, except for one (optionally).
    e.g. egge, egige, i

    Therefore, if k = 3, and there are '4' different characters with a count of 1, it is
    not possible. If there are '2', this is okay!
"""

def canConstruct(s: str, k: int) -> bool:
    # If the length of 's' is shorter than 'k', even splitting
    # 's' into individual characters will not be sufficient.
    if len(s) < k:
        return False
    
    c = Counter(s)
    uneven_num_total = 0

    for count in c.values():
        if count % 2 == 1:
            uneven_num_total += 1

    return uneven_num_total <= k
    
print(canConstruct("annabelle", 2))
print(canConstruct("leetcode", 3))
print(canConstruct("true", 4))
print(canConstruct("cr", 7))