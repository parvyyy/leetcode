# 12/1/25
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/

"""
    Use a stack, but this time add tuples, including the index. That is, ('(', '0').

    A valid parentheses string must have an equal number of '('s and ')'s. However, each
    ')' must have a corresponding '(' prior to it.
"""
def isValid(s: str, locked: str) -> bool:
    # Valid parentheses occur in '(' , ')' pairs. Hence the string
    # length must be a multiple of 2.
    if len(s) % 2 == 1:
        return False
    
    stack, unlocked = [], set()

    for (i, n) in enumerate(locked):
        if n == '0':
            unlocked.add(i)

    for (i, parentheses) in enumerate(s):
        match parentheses:
            case '(':
                stack.append((i, '('))

            # Flips ')' to '(' when necessary / possible.
            # If necessary, but impossible, returns False
            case ')':
                if len(stack) == 0:
                    if i in unlocked:
                        stack.append((i, '('))
                        unlocked.remove(i)
                    else:
                        print(i, stack)
                        return False
                else:
                    stack.pop()


    # Deals with cases where too many '(' due to flipping.
    final_stack = []

    for (i, parentheses) in stack:
        if len(final_stack) == 0:
            final_stack.append('(')
        else:
            if i in unlocked:
                final_stack.pop()
            else:
                final_stack.append('(')

    return len(final_stack) == 0

def isValidCorrect(s: str, locked: str):
    if len(s) % 2 == 1:
        return False
    
    # Notice that if a parentheses is locked, it cannot be changed. Those
    # that are not locked are able to be completely controlled!
    s = list(s)
    for (i, isLocked) in enumerate(locked):
        if isLocked == '0':
            s[i] = 'X'

    # Now, we must ensure that for every ')', there is sufficient space on it's left
    # to become '(', and similarly for every '(' there is sufficient space on it's right
    # to become ')'. We achieve this using a 'prefix sum'.
    sum_open = sum_closed = sum_free = 0
    for parentheses in s:
        sum_open += parentheses == '('
        sum_closed += parentheses == ')'
        sum_free += parentheses == 'X'

        if sum_closed > sum_open + sum_free:
            return False
        
    sum_open = sum_closed = sum_free = 0
    for parentheses in reversed(s):
        sum_open += parentheses == '('
        sum_closed += parentheses == ')'
        sum_free += parentheses == 'X'

        if sum_open > sum_closed + sum_free:
            return False

    return True






print(isValidCorrect("))()))", "010100"))
print(isValidCorrect("()()", "0000"))
print(isValidCorrect(")", "0"))
print(isValidCorrect("())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(", "100011110110011011010111100111011101111110000101001101001111"))
print(isValidCorrect("())()))()(()(((())(()()))))((((()())(())", "1011101100010001001011000000110010100101"))