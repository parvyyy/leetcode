# 7/1/25
# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

from collections import defaultdict
def queryResults(limit: int, queries: list[list[int]]) -> list[int]:
    # Maps each ball to it's colour.
    ball_to_colour = defaultdict(int)

    # Tracks the total # of each colour
    in_degree = defaultdict(int)

    results, curr = [], 0

    for ball, colour in queries:
        if prev_colour := ball_to_colour[ball]:
            in_degree[prev_colour] -= 1

            # If such a change results in the in-degree of the colour
            # dropping to 0, no instance of the colour exists.
            if in_degree[prev_colour] == 0:
                curr -= 1

        ball_to_colour[ball] = colour
        in_degree[colour] += 1

        # Represents a new colour being added -- the first instance!
        if in_degree[colour] == 1:
            curr += 1

        results.append(curr)

    return results

print(queryResults(4, [[1,4],[2,5],[1,3],[3,4]]))
print(queryResults(4, [[0,1],[1,2],[2,2],[3,4],[4,5]]))