def smallestNumber(pattern: str) -> str:
    n = len(pattern)

    def backtrack(idx: int) -> bool:
        if idx == n + 1:
            return True
        
        prevV, dirr = seq[idx - 1], pattern[idx - 1]

        if dirr == "I":
            lo, hi = prevV + 1, 10
        elif dirr == "D":
            lo, hi = 1, prevV

        for i in range(lo, hi):
            if used[i]:
                continue

            seq[idx], used[i] = i, True

            if backtrack(idx + 1):
                return True
            
            used[i] = False

        return False

    for start in range(1, 10):
        seq, used = [0] * (n + 1), [0] * 10
        seq[0], used[start] = start, True

        if backtrack(1):
            return "".join([str(v) for v in seq])

print(smallestNumber("IIIDIDDD"))
print(smallestNumber("DDD"))
print(smallestNumber("IID"))
print(smallestNumber("IDD"))