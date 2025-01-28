# 28/1/25
# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/

def findMaxFish(grid: list[list[int]]) -> int:
    nr, nc = len(grid), len(grid[0])

    def inBounds(r: int, c: int) -> bool:
        return 0 <= r < nr and 0 <= c < nc
    
    visited = [[False for _ in range(nc)] for _ in range(nr)]

    def DFS(src: tuple[int, int]) -> int:
        ri, ci = src

        visited[ri][ci] = True

        neighbout_cumulative = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rn, cn = ri + dr, ci + dc
            if not inBounds(rn, cn):
                continue

            if visited[rn][cn]:
                continue

            if grid[rn][cn] == 0:
                continue

            neighbout_cumulative += DFS((rn, cn))

        return neighbout_cumulative + grid[ri][ci]

    maxx = 0
    for (r, row) in enumerate(grid):
        for (c, cell) in enumerate(row):
            if visited[r][c]:
                continue

            if cell == 0:
                continue

            maxx = max(maxx, DFS((r, c)))

    return maxx

print(findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))
print(findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]))
print(findMaxFish([[10,5],[8,0]]))
print(findMaxFish([[4,5,5],[0,10,0]]))