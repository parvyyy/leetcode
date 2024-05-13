# n = len(s), m = len(words), k = len(words[0])
def findSubstring(s, words): # O(n * n * m)
  i, window_size = 0, len(words[0])
  start_idxs = []

  # Copying a dict is more efficient than creating it.
  g_word_tracker = dict()
  for word in words:
      g_word_tracker[word] = g_word_tracker.get(word, 0) + 1

  while i < (len(s) - (len(words) * window_size) + 1): # n - mk + 1 steps
    word_tracker = g_word_tracker.copy()

    j = i
    while j < len(s): # n / 3 steps
      windowed_word = s[j:j+window_size]

      if windowed_word in words and word_tracker[windowed_word] != 0: # m steps
        word_tracker[windowed_word] = word_tracker.get(windowed_word) - 1
        j += window_size
      else:
        break

    if all(key == 0 for key in word_tracker.values()): # m steps
      start_idxs.append(i)

    # Filler words are not guarenteed to be of `window-size`. Must increment by 1 & not window-size.
    i += 1

  return start_idxs

# Optimal Solution
def findSubstringOptimal(s, words):
   return
   

print(findSubstring("barfoothefoobarman", ["foo","bar"]))
print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
print(findSubstring("cvecqxjemfumiqgppzqadaduhzxwymeahkdzhodtvyhfqouipmitmlpvmmsmayniishpglkbltgbhclxptsdgjzvxrhxpufxmpouaavltdodgaaxvuccdbxauezlbhipwykwahjulxxtzzsvtuzyywasczefgovenfapmjjzjiukhmfchecfcczhedmmsjrhotwdfieqqzaalgeumhzrlzapemewwxfmqerxmwnevoggulbiuczfdbxiodgmaoasssqgqdklrtrnguwaxxfczekphrdjfdczxsfnvrypkscqoasnyaqzeaootrxawbzwtejrykiickbsltgltwmawaqstnsrpsnkyxdwjlhlykfldlwzhibgkryfgqwxkmkjlnhuzohzymkeygffqincznhhgfhqrrbcejyfxfeysoeqwjxornqsazbgfizyzadgjbljhsjzinrfwqtpdmjelkmqvlpumsaxtoicgrbqeuvclrtqdcwopjhkwwekqhklxsofkrvqorvbiornrobgzisxgyiyfskcmahytdphwkkgactrswzthrqnsaoxuychalfvqwdoipujrpclocevvxkpzypuyrdyeiuxhznroiaizftpjakgzvwyvlsuevskgohppvggfjogojwxlgdkdbjzmbvqznbfekwvhcbmlrvbdryozezffigujbkkqnpuylsfqtudnpfqifehjdorlulxvxhmlzilmascwogjdlzlsfvcjjvueitbfbpsayfmayrwmxhskifcocgxmdtslnvtqllsjrglrxifwpxiaflohtnvxgnkvldnwrfhkmsbjcgiugquldiuxvqwdfibqmomfuvpioqtqybkeservomulcsrhbsapgouckjmyzgqzjdgbjxzylvlpoczruzgdnahxjuxkcqjltppcnqcanoqbqpunoasdabdlxcvzsfnlucojsskfgcjzrdohggmgjpshspgkutyrxocrgmxpqiohncqtkdctswcmllzggxzenbvvoukgeaqscgnojpkenmszzrhgqgkfhhbxcleimuaqaqhmhrsvfmufgbnyjxeqgfoissrgotxqjeerxwoelilrlypuxvkecaovuhbibabmgfffetkpdxioyxkvvvbxxqssxwcawdnflskpoweruogslqpinrgnhafgyjhxpucaompcjvwfjcxwumfkfnxmnevmncjeyleoztrkqnpzroyndfziswxfcstsuewurbirwbdnqtohjmxmrwvjvurxmmpirmckpmblohyeanolzlytjveepxedktndhrnwdrirygwavmlxzjqigwpxutaeonjwgwukpcbnlzngnzfmkvxrumoohruvgdtnboxrqaedcumpvrefpbyjppxwirrowldxzcordtvhnjwkaarpdqashxorqifmvlkwnynqtkxitwswyklccoulnlcetjsouckidzaymahfwbbwnpyrdvcqggwbsprmtbwyczxozgwxjztzosqtpvmvbiytzpitsgtufsleahbkgxjxrbsgwedapbtoqdjikdcrxpwywzifwtenuwvrdyrszmgpsszexevutrsstczrvdhsbclgdeycqhukztoyzkstdllwpmqnrxfubqbeuzjmidxjylhyxatbngzcsppjoudsmewigfvoksyjfhjdhcguifzaxqlnnqfzxcidjftuztfebojksphcxgcuwpjlfplctvhcadyzwdfztpmngtpfbtbzillqawuttexthwufbzhvqtizmaentgmcrzut", ["hbkgxjxrbsgwedapbtoqdjikdc","rwbdnqtohjmxmrwvjvurxmmpir","qbeuzjmidxjylhyxatbngzcspp","mckpmblohyeanolzlytjveepxe","dktndhrnwdrirygwavmlxzjqig","abmgfffetkpdxioyxkvvvbxxqs","szexevutrsstczrvdhsbclgdey","wpxutaeonjwgwukpcbnlzngnzf","wumfkfnxmnevmncjeyleoztrkq","dohggmgjpshspgkutyrxocrgmx","lkwnynqtkxitwswyklccoulnlc","rxpwywzifwtenuwvrdyrszmgps","gqgkfhhbxcleimuaqaqhmhrsvf","rgnhafgyjhxpucaompcjvwfjcx","umpvrefpbyjppxwirrowldxzco","rdtvhnjwkaarpdqashxorqifmv","rxwoelilrlypuxvkecaovuhbib","zosqtpvmvbiytzpitsgtufslea","cqhukztoyzkstdllwpmqnrxfub","npzroyndfziswxfcstsuewurbi","bvvoukgeaqscgnojpkenmszzrh","sxwcawdnflskpoweruogslqpin","fzaxqlnnqfzxcidjftuztfeboj","pqiohncqtkdctswcmllzggxzen","mufgbnyjxeqgfoissrgotxqjee","etjsouckidzaymahfwbbwnpyrd","mkvxrumoohruvgdtnboxrqaedc","vcqggwbsprmtbwyczxozgwxjzt","joudsmewigfvoksyjfhjdhcgui"]))