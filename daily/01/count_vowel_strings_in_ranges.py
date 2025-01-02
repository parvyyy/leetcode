# https://leetcode.com/problems/count-vowel-strings-in-ranges/description/
# 02/01/25
"""
Have a running total, counting the # of words starting and ending w/ a vowel. 
Then, go through the words and map the index to the running total.

For each query, find the difference between the running total's (using l_i and r_i
as the key's) and add to a list.
"""
from collections import defaultdict

def vowelStrings(words: list[str], queries: list[list[int]]) -> list[int]:
    vowel_running_totals = defaultdict

    def isVowelStr(word: str) -> bool:
        def isVowel(letter: str) -> bool:
            return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'u' or letter == 'o'

        return isVowel(word[0]) and isVowel(word[-1])

    running_total = 0
    for (i, word) in enumerate(words):
        if isVowelStr(word):
            running_total += 1

        vowel_running_totals[i] = running_total

    in_range = []
    for query in queries:
        assert len(query) == 2

        # Subtract '1' from l_i, as the # of total vowel's should be inclusive of l_i,
        # hence, we do not want to find the difference with the l_i entry included.
        l_i, r_i = query[0] - 1, query[1]

        in_range.append(vowel_running_totals[r_i] - vowel_running_totals[l_i])

    return in_range

### Optimisation -- use a list instead of a dictionary, which is unnecessary.
### A list naturally maps the index to a value -- in this case, the running total.
### Will need to account for indexing at -1.

if __name__ == "__main__":
    print(vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]])) # [2, 3, 0]
    print(vowelStrings(["a", "e", "i"], [[0,2],[0,1],[2,2]])) # [3, 2, 1]

