from collections import defaultdict

def isIsomorphic(s, t):
  # A dict storing the indices of each letter. If the two are isomorphic, these
  # must have an equivalent set of values.

  s_letter_freq = defaultdict(list)
  t_letter_freq = defaultdict(list)

  if len(s) != len(t):
    return False
  
  for i in range(len(s)):
    s_letter_freq[s[i]].append(i)
    t_letter_freq[t[i]].append(i)

  # Improves efficiency
  if len(s_letter_freq.values()) != len(t_letter_freq.values()):
    return False
   
  for v in s_letter_freq.values():
    if v not in t_letter_freq.values():
      return False

  return True

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))