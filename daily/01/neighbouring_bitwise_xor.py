# 17/1/25
# https://leetcode.com/problems/neighboring-bitwise-xor/description/

"""
    Let's consider derived = [1,1,1,0,1,0,0,1]

    Then, original is = 
    [0, 1, 0, 1, 1, 0, 0, 0]
    [1, 0, 1, 0, 0, 1, 1, 1]

    Neither work as, until the final element, we can 'force' the original to work, but
    original[0] ^ original[n - 1] has been preset, and so it's result must align -- cannot be controlled.

    Whichever of the above we start with does not change, as they are simple ~ of each other.

    So, start with 0 and then, if:
        * derived[i] is '1', flip
        * derived[i] is '0', do nothing

    Then finally, the final answer will be if 0 ^ bit = derived[n - 1]
"""

def doesValidArrayExist(derived: list[int]) -> bool:
    tracking_bit = 0b0

    for n in derived[:-1]:
        if n == 1:
            tracking_bit ^= 1

    # '0' represents original[0], whilst the tracking bit represent original[n - 1]
    return tracking_bit ^ 0 == derived[-1]

print(doesValidArrayExist([1,1,0]))
print(doesValidArrayExist([1,1]))
print(doesValidArrayExist([1,0]))
print(doesValidArrayExist([1,1,1,0,1,0,0,1]))
print(doesValidArrayExist([1,1,1,0,1,0,0,0]))