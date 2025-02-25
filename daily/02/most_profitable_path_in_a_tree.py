# 24/02/25
# https://leetcode.com/problems/most-profitable-path-in-a-tree/description/

from functools import reduce
import math
def mostProfitablePath(edges: list[list[int]], bob: int, amount: list[int]) -> int:
    nV = max(reduce(lambda x, y: x + y, edges))
    g = [[] for _ in range(nV + 1)]

    for (v, w) in edges:
        g[v].append(w)
        g[w].append(v)

    def DFS(v: int, dest: int, path: list):
        visited[v] = True

        if v == dest:
            path.append(v)
            return True, path

        for neighbour in g[v]:
            if visited[neighbour]:
                continue

            path.append(v)

            res, path = DFS(neighbour, dest, path)
            if res:
                return True, path
            
            path.pop()

        return False, path

    visited = [False for _ in range(nV + 1)]
    _, path = DFS(bob, 0, [])

    print(path)

    bob_path = {
        v: i for (i, v) in enumerate(path)
    }

    # A leaf node has 1 out-degree in a tree.
    leaves = []
    for (v, neighbours) in enumerate(g):
        # The '0'th node is a special case -- the root!
        if v == 0:
            continue

        if len(neighbours) == 1:
            leaves.append(v)

    max_cost = -math.inf
    for leaf in leaves:
        ### Optimisations:
        #   Primary optimisation is to not DFS (O(n)) for each
        #   leaf node. Instead, use a BFS to explore all.

        visited = [False for _ in range(nV + 1)]
        _, alice_path = DFS(0, leaf, [])

        cost = 0
        for (i, n) in enumerate(alice_path):
            if n not in bob_path:
                cost += amount[n]
            else:
                j = bob_path[n]

                if i < j:
                    cost += amount[n]
                elif i == j:
                    cost += (amount[n] // 2)
                else:
                    cost += 0

        max_cost = max(max_cost, cost)
    
    return max_cost

print(mostProfitablePath([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6]))



    

