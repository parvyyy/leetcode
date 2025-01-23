# 23/1/25
# https://leetcode.com/problems/count-servers-that-communicate/description/

def countServers(grid: list[list[int]]) -> int:
    nr, nc = len(grid), len(grid[0])
    rows, cols = [0] * nr, [0] * nc

    for r in range(nr):
        for c in range(nc):
            rows[r] += grid[r][c]
            cols[c] += grid[r][c]

    count = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c]:
                count += rows[r] > 1 or cols[c] > 1
    
    return count

print(countServers([[1,0],[0,1]]))
print(countServers([[1,0],[1,1]]))
print(countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))
