from typing import Optional, ListNode
from collections import defaultdict

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
  frequencies = defaultdict(int)

  # First pass - Record the frequency of each value into 'frequencies'.
  curr = head
  while curr:
    frequencies[curr.val] += 1
    curr = curr.next
  
  curr = head
  while curr:
    if frequencies[curr.val] > 1:
      # Adjusts the position of the head, if deleted.
      if curr == head:
        head = head.next
      else:
        prev.next = curr.next

      curr = curr.next
    
    else:
      prev, curr = curr, curr.next

  return head