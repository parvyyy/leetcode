# 18/1/2025
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/

import heapq
import math
def minCost(grid: list[list[int]]) -> int:
    q = PriorityQueue()
    predecessor = [[(-1, -1) for _ in range(len(row))] for row in range(len(grid))]
    costs = [[math.inf for _ in range(len(row))] for row in range(len(grid))]


    
    pass

def minCostDijikstra(grid: list[list[int]]) -> int:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    n_r, n_c = len(grid), len(grid[0])

    # Priority queue, with elements added as: (cost, (r, c))
    pq = [(0, (0, 0))]
    min_cost = [[math.inf] * n_c for _ in range(n_r)]
    min_cost[0][0] = 0

    while pq:
        cost, (row, col) = heapq.heappop(pq)

        # Skip if we've found a better path to this cell.
        if min_cost[row][col] != cost:
            continue

        # Try all four directions
        for d, (dx, dy) in enumerate(dirs):
            new_row, new_col = row + dx, col + dy

            if 0 <= new_row < n_r and 0 <= new_col < n_c:
                new_cost = cost
                
                # Add 1 to cost if we need to change direction
                if d != (grid[row][col] - 1):
                    new_cost = cost + 1

                # Update if we found a better path -- edge relaxation.
                if new_cost < min_cost[new_row][new_col]:
                    min_cost[new_row][new_col] = new_cost
                    heapq.heappush(pq, (new_cost, (new_row, new_col)))

    return min_cost[n_r - 1][n_c - 1]