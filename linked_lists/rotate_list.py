from typing import Optional, ListNode

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
  # First pass - Determine the length of the LL.
  curr, n = head, 0
  while curr:
    curr, n = curr.next, n + 1

  # Empty List
  if n == 0:
    return head

  k = k % n

  # No rotation
  if k == 0:
    return head

  curr, i = head, 0
  while curr:
    # Seperate the LL at the 'new end'
    if i == n - k:
      prev.next = None
      new_head = curr

    i += 1
    prev, curr = curr, curr.next

  # Attach the end of the new 'starting-LL' to the start of the older LL.
  prev.next = head
  
  return new_head