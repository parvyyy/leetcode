def lengthOfLongestSubstring(s):
  # Set the start of the window to the first element.
  # Increase the sliding window until a non unique element (use a Hashmap for O(1) checking)
  # Once a duplicate is found, record the length - replacing the max if greater
  # Move the start of the sliding window once to the right and repeat
  start, end = 0, 0
  maxLen = 0

  substr_dict = dict()

  for start in range(0, len(s)):
    # The loc_max should not be reset to 0 as the region from start -> end (i.e. current substr) is not
    # necessarily zero.

    loc_max = len(substr_dict.keys())

    while end < len(s) and s[end] not in substr_dict:
      substr_dict[s[end]] = True

      end += 1
      loc_max += 1

    maxLen = max(maxLen, loc_max)
    substr_dict.pop(s[start])

  return maxLen

print(lengthOfLongestSubstring("dvdf")) # 3
print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("bbbbb")) # 1
print(lengthOfLongestSubstring("pwwkew")) # 3