from typing import Optional

# Custom `Node` implementation w/ `random` field.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# NOTE: This sol has O(n) space complexity & does FOUR passes.
#       Optimised solutions can do ONE/TWO passes & O(1) space complexity.
#       More info here: https://neetcode.io/problems/copy-linked-list-with-random-pointer/solution
def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    def getNodeIdx(head: Optional[Node]) -> dict[Node, int]:
        nodes_to_idx = dict()

        curr, idx = head, 0
        while curr:
            nodes_to_idx[curr] = idx

            curr = curr.next
            idx += 1

        return nodes_to_idx

    nodes: tuple[int, int] = []
    nodes_to_idx = getNodeIdx(head)

    curr = head
    while curr:
        random_idx = None
        if curr.random:
            random_idx = nodes_to_idx[curr.random]

        nodes.append((curr.val, random_idx))
        curr = curr.next

    # Create a deep copy of the LL
    copied_nodes: list[Node] = []

    head = Node(0)
    curr = head

    for v, _ in nodes:
        curr.next = Node(v)
        curr = curr.next

        copied_nodes.append(curr)

    for i in range(len(copied_nodes)):
        random_idx, random = nodes[i][1], None

        if random_idx != None:
            random = copied_nodes[random_idx]

        copied_nodes[i].random = random

    return head.next
