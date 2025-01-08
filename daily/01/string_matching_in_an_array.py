# https://leetcode.com/problems/string-matching-in-an-array/description/
# 7/1/25
"""
    Naive:
        Sort the words list by length (nlogn).

        Clearly, as all strings are unique, the words w/ the longest length
        cannot be substrings of another.

        For each following word, iterate through words (O(n^2)).
        
        If the current word is a substr of the pointed-to word, add to a list
        and continue.
"""

def stringMatching(words: list[str]) -> list[str]:
    words = sorted(words, key=len, reverse=True)
    matches = []

    for (i, word) in enumerate(words):
        for (j, another_word) in enumerate(words):
            # As it has been sorted by length, we know that
            # all elements to the right of index i, will have
            # equal or lesser length, and hence 'word' cannot be a
            # substring of them. Does not improve time complexity, but
            # prevents meaningless work.
            if i == j:
                break

            if word in another_word:
                matches.append(word)
                break

    return matches

print(stringMatching(["mass","as","hero","superhero"]))
print(stringMatching(["leetcode","et","code"]))

