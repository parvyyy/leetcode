# 10/1/25
# https://leetcode.com/problems/clear-digits/description/

def clearDigits(s: str) -> str:
    letters = []

    for v in s:
        if v.isnumeric():
            letters.pop()
        
        if v.isalpha():
            letters.append(v)

    return ''.join(letters)

print(clearDigits("abc"))
print(clearDigits("cb34"))
print(clearDigits("cba34"))