def countPrefixSuffixPairs(words: list[str]) -> int:
    total = 0

    def isPrefixAndSuffix(fix: str, s: str):
        if len(fix) > len(s):
            return False
        
        n = len(fix)
        return fix == s[:n] and fix == s[-n:]

    # Naive solution
    for (i, fix) in enumerate(words):
        for (j, word) in enumerate(words):
            if i >= j:
                continue

            total += isPrefixAndSuffix(fix, word)

    return total

print(countPrefixSuffixPairs(["a","aba","ababa","aa"]))
print(countPrefixSuffixPairs(["pa","papa","ma","mama"]))
print(countPrefixSuffixPairs(["abab","ab"]))