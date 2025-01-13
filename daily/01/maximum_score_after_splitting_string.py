
def maxScore(s: str) -> int:
    zero_count, one_count = 0, len(list(filter(lambda x: x == '1', s)))
    max_score = 0

    for v in s:
        zero_count += v == '0'
        one_count -= v == '1'

        max_score = max(max_score, zero_count + one_count)

    return max_score

print(maxScore("011101"))