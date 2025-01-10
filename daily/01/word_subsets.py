# 10/1/25
# https://leetcode.com/problems/word-subsets/

from typing import List
from collections import Counter, defaultdict

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    """
        Create a hashmap storing the cultimiate frequency of letters, but only tracking
        the max of the letter. This is as, if the word can fulfil the criteria of 'a: 2',
        this automatically ensures it fulfils 'a: 1'.
    """

    ### Concise way to combine Counters, rather than using a defaultdict
    # c = Counter()
    # for w in words2:
    #     c |= Counter(w)

    cumulative_letter_distribution = defaultdict(int)
    for word in words2:
        word_distribution = Counter(word)

        for (k, count) in word_distribution.items():
            if count > cumulative_letter_distribution[k]:
                cumulative_letter_distribution[k] = count
    
    universal_words = set(words1)
    for word in words1:
        word_distribution = Counter(word)

        # To remove the 'flag' variable, could invert the problem. That is, start with all
        # words considered to be 'universal'. When they fail the criteria, remove them. Using
        # a set achieves this in O(1) time.
        for (k, count) in cumulative_letter_distribution.items():
            if cumulative_letter_distribution[k] > word_distribution[k]:
                universal_words.remove(word)
                break
           
    return list(universal_words)

print(wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
print(wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"]))