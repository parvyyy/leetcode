def hasMatch(s: str, p: str) -> bool:
    l, r = p.split('*')
    l_idx, r_idx = s.find(l), s.rfind(r)

    # Addresses cases like *u or u*
    if (not l and r_idx != -1) or (not r and l_idx != -1):
        return True

    if l_idx == -1 or r_idx == -1:
        return False
    
    # Accounts for multi-letter patterns, but reduces 1 as * may be 'blank' (i.e. 0 characters)
    return l_idx + len(l) - 1 < r_idx

print(hasMatch("leetcode", "ee*e"))
print(hasMatch("car", "c*v"))
print(hasMatch("luck", "u*"))
print(hasMatch("ojjju", "*o"))