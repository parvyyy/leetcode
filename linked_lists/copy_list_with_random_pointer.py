from typing import Optional

class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random


# Essentially, we use a Hashmap to store the access the nodes (without re-traverseing the list).
# This is done by storing the original node as the key, and its corresponding duplicate as the value.
def copyRandomList(head: Optional[Node]) -> Optional[Node]:
  curr = head
  copier = new_head = Node(-1)

  node_map = dict()

  # First-pass, adding all the nodes (& their .val)
  while curr:
    copier.next = Node(curr.val)
    # With the key of the Node, store the new DUPLICATE node 
    node_map[curr] = copier.next

    curr, copier = curr.next, copier.next
    

  curr, copier = head, new_head.next

  # Second-pass, using the hashmap of original nodes to linked nodes, attach .random nodes.
  while curr:
    if curr.random:
      # Assign the properties of the corresponding node (i.e. curr.random) onto the duplicate node
      copier.random = node_map[curr.random]
    

    curr, copier = curr.next, copier

  return new_head.next