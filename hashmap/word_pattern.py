def wordPattern(pattern, s):
  letter_to_word_dict = dict()

  words = s.split(' ')

  for idx, letter in enumerate(pattern):
    if letter not in letter_to_word_dict.keys(): #O(1) as set.

      # If an already mapped word is being assigned to another letter.
      if words[idx] in letter_to_word_dict.values():
        return False
      
      letter_to_word_dict[letter] = words[idx]
      continue

    if letter_to_word_dict[letter] != words[idx]:
      return False


  return True

print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
print(wordPattern("aaaa", "dog cat cat dog"))