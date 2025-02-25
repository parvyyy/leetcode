# 19/2/25
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

def getHappyString(n: int, k: int) -> str:
  letters = ['a', 'b', 'c']
  seqs = []

  def getNextLetter(idx: int):
    if idx == n:
      seqs.append("".join(seq))
      return

    for l in letters:
      if l == seq[idx - 1]:
        continue


      seq.append(l)

      getNextLetter(idx + 1)

      seq.pop()

    return

  for l in letters:
    seq = [l]
    getNextLetter(1)

  if k > len(seqs):
    return ""

  return seqs[k - 1]

print(getHappyString(1, 3))
print(getHappyString(1, 4))
print(getHappyString(3, 9))