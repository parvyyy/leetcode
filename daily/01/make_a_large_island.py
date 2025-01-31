# 31/1/25
# https://leetcode.com/problems/making-a-large-island/description/

from collections import deque

def largestIsland(grid: list[list[int]]) -> int:
    nr, nc = len(grid), len(grid[0])

    # Maps the cell to the component_no, component_nV
    island_sizes = [[(-1, 0) for _ in range(nc)] for _ in range(nr)]

    def inBounds(r: int, c: int) -> bool:
            return 0 <= r < nr and 0 <= c < nc

    def BFS(root: tuple[int, int]):
        q = deque([root])
        visited.add(root)

        while q:
            rr, rc = q.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r, new_c = rr + dr, rc + dc

                if not inBounds(new_r, new_c):
                    continue

                if (new_r, new_c) in visited:
                    continue

                if grid[new_r][new_c] == 0:
                    continue

                q.append((new_r, new_c))
                visited.add((new_r, new_c))

    island_no = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == 0:
                continue

            island_id, _ = island_sizes[r][c]

            # Acts as a 'global-visited' array.
            if island_id != -1:
                continue

            # A local 'visited' set used to track the cells visited
            # in this BFS iteration.
            visited = set()
            BFS((r, c))

            for rr, rc in visited:
                island_sizes[rr][rc] = (island_no, len(visited))

            island_no += 1

    maxx = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c]:
                continue

            neighbours = set()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                rr, rc = r + dr, c + dc

                if not inBounds(rr, rc):
                    continue

                neighbours.add(island_sizes[rr][rc])

            # Removes the island_no, which was used to filter duplicates
            # but transforms to list, to not remove different islands with 
            # the same count.
            neighbours = [v for (_, v) in neighbours]

            maxx = max(maxx, sum(neighbours) + 1)

    # No '0''s were found -- return max island.
    if maxx == 0:
        return nr * nc

    return maxx

print(largestIsland([[1,0],[0,1]]))
print(largestIsland([[1,1],[1,0]]))
print(largestIsland([[1,1],[1,1]]))
print(largestIsland([[0,0],[0,0]]))
print(largestIsland([[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],
                     [1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],
                     [0,1,1,1,1,0,0]]))