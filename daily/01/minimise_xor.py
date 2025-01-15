# 15/1/25
# https://leetcode.com/problems/minimize-xor/description/

"""
    Let's consider there are 'y' set bits in num2.

    To minimise x XOR num1, the leading bits must all be 0 for as long as possible.
    These affect the # to the most degree.

    This is achieved by matching the 0's and the 1's.

    To count the # of 1's in Python, we can do str(int(a, 2))

    Start x on nums1. Perform a left pass, matching each number until the 1's
    count is satisfied. Pad the remaining number with 0's.

    If the 1's count is NOT satisfied, perform a right pass, flipping 0's to 1's
    until the 1's count is satisfied.
"""

def minimiseXOR(num1: int, num2: int) -> int:
    diff = num1.bit_count() - num2.bit_count()

    # If the set bits are equal, nums1 |= nums1 == 0.
    if diff == 0:
        return num1
    
    x = f"{num1:032b}"

    # If there are additional 1's in num1, we must replace the trailing
    # 'diff' amount of 1's with 0's.
    if diff > 0:
        x = x[::-1]
        x = x.replace('1', '0', diff)
        x = x[::-1]

    # If there are additional 1's in num2, we must replace the trailing
    # 'diff' amount of 0's with 1's.
    else:
        x = x[::-1]
        x = x.replace('0', '1', -diff)
        x = x[::-1]
        
    x = int(f'0b{x}', 2)

    return x

print(minimiseXOR(3, 5))
print(minimiseXOR(1, 12))