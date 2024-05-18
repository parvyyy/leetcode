from typing import List
from collections import defaultdict
# from valid_anagram import isAnagram

def groupAnagrams(strs: List[str]) -> List[List[str]]:
  # Naive: mn^2
  # My sol: mn * log(m)
  ordered_strs = strs.copy()

  for idx, word in enumerate(ordered_strs):
    ordered_strs[idx] = ''.join(sorted(word))

  # The sorted word is the key for the dict.
  groups = defaultdict(list)

  for idx, word in enumerate(strs):
    groups[ordered_strs[idx]].append(word)

  return groups.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))