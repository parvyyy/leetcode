# 11/2/25
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

def removeOccurrences(s: str, part: str) -> str:
    n, p = len(s), len(part)
    i, j = 0, len(part)

    if s == part:
        return ''

    while j <= n:
        window = s[i:j]

        if window != part:
            i, j = i + 1, j + 1
            continue

        # Remove the substring.
        s = s[:i] + s[j:]

        # For instant-matches! Works in Python as -1 (etc) are valid 
        # indices, but not language-agnostic without clamping i & j.
        i, j = max(0, i - p), max(p, j - p)

    return s


print(removeOccurrences("ccctltctlltlb", "ctl"))
print(removeOccurrences("xyxyxyxyb", "xyb"))
print(removeOccurrences("daabcbaabcbc", "abc"))
print(removeOccurrences("axxxxyyyyb", "xy"))
print(removeOccurrences("axyxyxyxyb", "xy"))
print(removeOccurrences("xyxyxyxyb", "xy"))
print(removeOccurrences("xyxyxyxyb", "cd"))
print(removeOccurrences("aaaaaa", "a"))
print(removeOccurrences("a", "a"))
print(removeOccurrences("a", "ab"))