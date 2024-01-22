def isMatchingPair(symbol, pair):
    if symbol == "(" and pair == ")":
        return True
    
    if symbol == "{" and pair == "}":
        return True
    
    if symbol == "[" and pair == "]":
        return True
    
    return False

def isValidParentheses(s):
    stack = []

    opening_symbols = ["(", "{", "["]
    closing_symbols = [")", "}", "]"]

    for symbol in s:
        if symbol in opening_symbols:
            stack.append(symbol)
            
        elif symbol in closing_symbols:
            if not stack:
                return False

            if not isMatchingPair(stack.pop(), symbol):
                return False
    
    return len(stack) == 0


def main():
    print(isValidParentheses("()[]{}"))
    print(isValidParentheses("()[]{({{()}})}"))
    print(isValidParentheses("()[]{({{(])}})}"))

    return 0

if __name__ == "__main__":
    main()       