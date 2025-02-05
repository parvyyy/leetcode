# 5/1/25
# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

def areAlmostEqual(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    t1, t2 = set(enumerate(s1)), set(enumerate(s2))
    t1, t2 = t1 - t2, t2 - t1

    if len(t1) == len(t2) == 0:
        return True
    
    if len(t1) == len(t2) == 2:
        (i1,  c1), (i2, c2) = t1

        if (i1, c2) in t2 and (i2, c1) in t2:
            return True
        
    return False

print(areAlmostEqual("bank", "kanb"))
print(areAlmostEqual("attack", "defend"))
print(areAlmostEqual("kelb", "kelb"))
print(areAlmostEqual("ran", "rann"))
print(areAlmostEqual("quick", "quikk"))