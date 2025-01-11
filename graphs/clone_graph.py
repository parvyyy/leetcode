from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    # As the graph is connected, it is not necessary to account for 
    # other components. Furthermore, the 'val' is unique for each node.
    if not node:
        return None
    
    # Run a BFS from node, creating the graph as you traverse.
    queue: deque[Node] = deque()
    queue.append(node)

    # Maps the value of the node to the newly created Node obj's.
    clones = {
        node.val: Node(node.val)
    }

    while len(queue) != 0:
        vertex = queue.popleft()

        curr_node = clones[vertex.val]

        for neighbour in vertex.neighbors:
            if neighbour.val in curr_node:
                continue

            queue.append(neighbour)
            clones[neighbour.val] = Node(neighbour.val)

            # This way, when referencing the node with '1', we are appending
            # the SAME obj, which is stored in clones!
            curr_node.neighbors.append(clones[neighbour.val])

    return clones[node.val]