# 22/1/25
# https://leetcode.com/problems/map-of-highest-peak/

from collections import deque
import math


# This is O((mn) ** 2) in the worst-case. Instead of a new BFS for each water cell --
# add all water cells to the queue before starting the BFS. This also prevents the need
# to take the minimum of the prev + 1 vs. current.

def highestPeak(isWater: list[list[int]]) -> list[list[int]]:
    n_r, n_c = len(isWater), len(isWater[0])

    # Starting at each water cell, run a BFS & store the # of steps
    # within each value. Take the minimum of it.

    topography = [[math.inf for _ in range(len(row))] for row in isWater]

    def BFS(src: tuple[int, int]):
        visited = [[False for _ in range(len(row))] for row in isWater]
        q = deque()

        q.append(src)
        visited[src[0]][src[1]] = True
        topography[src[0]][src[1]] = 0

        def inBounds(r: int, c: int) -> bool:
            return 0 <= r < n_r and 0 <= c < n_c

        while q:
            r, c = q.popleft()

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + dr, c + dc

                if not inBounds(new_r, new_c):
                    continue

                if visited[new_r][new_c]:
                    continue

                if isWater[new_r][new_c]:
                    continue

                visited[new_r][new_c] = True

                topography[new_r][new_c] = min(
                    topography[r][c] + 1, 
                    topography[new_r][new_c]
                )

                q.append((new_r, new_c))

    for (i, row) in enumerate(isWater):
        for (j, cell) in enumerate(row):
            if cell:
                BFS((i, j))

    
    return topography
                

def highestPeakOptimised(isWater: list[list[int]]) -> list[list[int]]:
    n_r, n_c = len(isWater), len(isWater[0])

    q = deque()
    topography = [[-1 for _ in range(len(row))] for row in isWater]

    # Add all water cells to the queue.
    for (r, row) in enumerate(isWater):
        for (c, cell) in enumerate(row):
            if cell:
                q.append((r, c))
                topography[r][c] = 0

    def inBounds(r: int, c: int) -> bool:
        return 0 <= r < n_r and 0 <= c < n_c
    
    # Perform a BFS -- O(mn) operation. Each cell essentially is given a value corresponding
    # to the minimum # of steps to the nearest water cell.
    while q:
        r, c = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = r + dr, c + dc

            if not inBounds(new_r, new_c):
                continue

            # Topography also acts as a 'visited' array, where a '-1' value implies
            # that the cell has not yet been visited.
            if topography[new_r][new_c] >= 0:
                continue

            if isWater[new_r][new_c]:
                continue

            topography[new_r][new_c] = topography[r][c] + 1
            q.append((new_r, new_c))
    
    return topography

print(highestPeakOptimised([[0,1],[0,0]]))
print(highestPeakOptimised([[0,0,1],[1,0,0],[0,0,0]]))
