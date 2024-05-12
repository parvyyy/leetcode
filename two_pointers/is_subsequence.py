def isSubsequence(s, t):
  s_idx = 0

  for letter in t:
    if s_idx is len(s):
      return True
    
    if letter is s[s_idx]:
      s_idx = s_idx + 1
  
  return False

# ORIGINAL ATTEMPT - Overcomplicated the Q.
  # Naive: Strip out all letters from t that are not a part of s. - O(mn)
  # Then, if there is a contiguous chunk containing s, return true, otherwise false.

  # filtered_t = ''

  # for letter in t:
  #   if letter in s:
  #     filtered_t = filtered_t + letter

  # # Cannot simply return 's in filtered_t'.
  # # Counter-Example: 'aec' is a subsequence of 'aaaeeeccc' despite 'aec in aaaeeeccc' being False.
  # # We cannot remove duplicates as 'aaaaec' is NOT a subsequence of 'aaaeeeccc'.
  

  # # Solution: 
  # # 1. Check the frequency of letters in filtered_t > frequency of letters in s.
  # # 2. Filter filtered_t for duplicates - without changing order.
  # # 3. Check if s is contained in filtered_t.

  # for letter in s:
  #   if filtered_t.count(letter) < s.count(letter):
  #     return False

  # # FIXME: Does not maintain order, and hence 'aec' & 'ace' both return True.
  # s = str(dict.fromkeys(s))
  # filtered_t = str(dict.fromkeys(filtered_t))

  # return s in filtered_t

print(isSubsequence("acb", "ahbgdc")) # False
print(isSubsequence("ace", "abcde")) # True
print(isSubsequence("aec", "abcde")) # False
print(isSubsequence("abc", "ahbgdc")) # True
print(isSubsequence("axc", "ahbgdc")) # False
print(isSubsequence("leeeeetcode", "leeeeeetcode")) # True