from collections import defaultdict

def isAnagram(s, t):
  if len(s) != len(t):
    return False
  
  letter_frequencies = defaultdict(int)
  
  for i in range(len(s)):
    letter_frequencies[s[i]] += 1
    letter_frequencies[t[i]] -= 1


  return all(freq == 0 for freq in letter_frequencies.values())

print(isAnagram("anagram", "naagram"))
print(isAnagram("car", "rat"))

