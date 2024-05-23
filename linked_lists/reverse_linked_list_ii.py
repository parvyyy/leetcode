from typing import Optional, ListNode

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
  idx_to_value = dict()
  curr, idx = head, 0

  left, right = left - 1, right - 1 # 0 -indexing
  
  # First pass - Adding the values of the Node to a hashmap (mapped by index)
  while curr:
    if idx >= left and idx <= right:
      idx_to_value[idx] = curr.val

    curr, idx = curr.next, idx + 1

  # Second pass - Reversing
  curr, idx= head, 0

  while curr:
    # Reverse the values stored
    if idx >= left and idx <= right:
      curr.val = idx_to_value[right - (idx - left)]
      
    curr, idx = curr.next, idx + 1