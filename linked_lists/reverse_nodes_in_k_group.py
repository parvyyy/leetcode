from typing import Optional, ListNode
from reverse_linked_list_ii import reverseBetween

def reverseBetweenM(head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
  l, r = l - 1, r - 1 # 0 - indexing

  idx_to_node = dict()
  curr, idx = head, 0

  while curr:
    if idx >= l and idx <= r:
      idx_to_node[idx] = curr 

    curr, idx = curr.next, idx + 1

  return head

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
  # Perform Reverse Linked List (List, left, right) repeatly.

  curr, i = head, 1 # 1 - index counting (for modulo)
  
  while curr:
    if i % k == 0:
      l, r = i - k + 1, i
      # This modifies the VALUES, not the nodes themselves.
      reverseBetweenM(head, l, r) # This function takes l, r to be 1-indexed.

    curr, i = curr.next, i + 1

  return head