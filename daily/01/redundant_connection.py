# 29/1/25
# https://leetcode.com/problems/redundant-connection/description/

from collections import defaultdict

type Graph = defaultdict[int, list[int]]

class UnionFind():
    # Includes path compression
    def __init__(self, nV: int):
        assert nV > 0

        # Initially, every node is a root node
        self.parent = [i for i in range(nV)]

    # Joins groups x, y. Set's their representative / parent
    # to the same -- the parent of 'x'. O(logN) time complexity.
    def union(self, x: int, y: int) -> None:
        self.parent[self.find(y)] = self.find(x)

    # Finds the group x belongs to - it does this by returning the
    # representative of the group! The representative is the 'Parent'.
    # O(logN) time complexity
    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        
        root = self.find(self.parent[x])

        # Path compression -- for all nodes between x & the parent...
        while root != x:
            next_node = self.parent[x]

            # Set their parent to the true parent! Reduces tree height.
            self.parent[x] = root
            x = next_node

        return self.parent[x]

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def __str__(self):
        return str(self.parent)
    
def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    # Inspired by Kruskal's MST
    nV = max([max(e) for e in edges])
    u = UnionFind(nV)

    # O(logN)
    def hasCycle(v: int, w: int):
        # If an edge exists between u-v AND they are traced back to the same parent (p),
        # this forms a cycle from p-u u-v v-p.
        if u.connected(v, w):
            return True
        
        # Otherwise, they are both reachable from a common parent.
        u.union(v, w)

        return False

    for (v, w) in edges:
        # 0-index the vertices.
        if hasCycle(v - 1, w - 1):
            return [v, w]
        
    return -1

print(findRedundantConnection([[1,2],[1,3],[2,3]]))
print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))