from typing import List
def concatenate_string(s: str, res: List[str]) -> List[str]:
  if res == []:
    return [s]
  
  for (idx, sentence) in enumerate(res):
    res[idx] = s + ' ' + sentence

  return res

def performWordBreak(s: str, wordDict: set[str]):
  permutations = []

  if s == '':
    return permutations

  for i in range(len(s)):
    if s[:i + 1] in wordDict:
      res = performWordBreak(s[i + 1:], wordDict)
      
      if res is not None:
        res = concatenate_string(s[:i + 1], res)
        for entry in res:
          permutations.append(entry)

  return None if len(permutations) == 0 else permutations

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
  wordDict = set(wordDict)

  res = performWordBreak(s, wordDict)

  if res:
    return res
  
  return []


print(wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
print(wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))

  # Sliding window & recursion
  # The original sliding window is of size 0. Increase its size by 1 each loop.
  # If the word within the sliding window is in the wordDict
    # Recurse and call wordBreak(s[i:], dict)
    # Terminating Cond:
    # Concatenate the string onto each entry in the list

  # Example: catsanddog
  
'''
wordBreak("catsanddog", d) -> 'c', 'ca', 'cat'
  wordBreak('sanddog', d) -> 's', 'sa', 'san', sand'
    wordBreak('dog') -> 'd', 'do', 'dog'
      wordBreak('')
      if res is None:
        return None

      else s[:i].concat(res) (i.e. add s[:i] to the start of each word)

      []
        []

  -> 'cats'
  wordBreak('anddog', d)
'''


