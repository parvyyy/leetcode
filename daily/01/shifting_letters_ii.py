def shiftingLetters(s: str, shifts: list[list[int]]) -> str:
    cumulative_idx_shift = [0] * (len(s) + 1)

    for start, end, direction in shifts:
        ### Optimisations
        # Instead of iterating through from start to end to increment the shift,
        # we can instead increase the start by 1, and decrease end + 1 by 1.
        # Then, this array can instead be treated as a prefix sum to appropriately
        # handle the shift.
        if direction == 1:
            cumulative_idx_shift[start] += 1
            cumulative_idx_shift[end + 1] -= 1
        elif direction == 0:
            cumulative_idx_shift[start] -= 1
            cumulative_idx_shift[end + 1] += 1

    shifted_s = ''
    cumulative_sum = 0
    for i, letter in enumerate(s):
        cumulative_sum += cumulative_idx_shift[i]
        shifted_s += chr(((ord(letter) - ord('a') + cumulative_sum) % 26) + ord('a')) 

    return shifted_s

print(shiftingLetters("abc", [[0,1,0],[1,2,1],[0,2,1]]))
print(shiftingLetters("dztz", [[0,0,0],[1,1,1]]))