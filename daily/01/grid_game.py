# 21/1/25
# https://leetcode.com/problems/grid-game/description/

import math

### Optimisations
#   Storing a prefix & postfix list is unnecessary. Instead, in one iteration,
#   you may use two counters -- one for the prefix, the other postfix to find the
#   minimum of the maximum of the two paths.
#   Overall time complexity remain O(n), however space complexity is O(1) from O(n)

def gridGamePS(grid: list[list[int]]) -> int:
    n_r = len(grid[0])
    ps_1, ps_2 = [0] * n_r, [0] * n_r

    # Prefix sum of the first row.
    for i in range(n_r):
        if i == 0:
            ps_1[i] = grid[0][i]
            continue

        ps_1[i] = grid[0][i] + ps_1[i - 1]

    # Postfix sum of the second row.
    for i in range(n_r):
        i = n_r - i - 1

        if i == n_r - 1:
            ps_2[i] = grid[1][i]
            continue

        ps_2[i] = grid[1][i] + ps_2[i + 1]

    # Compare the top and bottom path, split by the transition 'down' at i.
    # Find where the maximum of the top & bottom path [as this is the one which
    # Robot 2 will optimally take] is the minimum!
    minn = math.inf
    for i in range(n_r):
        l = ps_2[0] - ps_2[i]
        r = ps_1[n_r - 1] - ps_1[i]

        minn = min(max(l, r), minn)

    return minn

### FUTURE IDEA:
# via DP
def gridGame(grid: list[list[int]]) -> int:
    dp = [[0 for _ in range(len(row))] for row in grid]

    dp[0][0] = grid[0][0]

    for (i, row) in enumerate(grid):
        for (j, cell) in enumerate(row):
            if i == 0 and j == 0:
                dp[i][j] = grid[0][0]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + cell
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + cell
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + cell

    print(dp)
            
print(gridGamePS([[2,5,4],[1,5,1]]))
print(gridGamePS([[3,3,1],[8,5,2]]))
print(gridGamePS([[1,3,1,15],[1,3,3,1]]))