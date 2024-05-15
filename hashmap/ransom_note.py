def canConstruct(ransomNote, magazine):
  letter_dict = dict()

  if len(ransomNote) > len(magazine):
    return False

  for l in magazine:
    letter_dict[l] = letter_dict.get(l, 0) + 1

  for l in ransomNote:
    if l not in letter_dict or letter_dict[l] == 0:
      return False
    
    letter_dict[l] -= 1

  return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))