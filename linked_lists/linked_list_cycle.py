from typing import Optional, ListNode

def hasCycle(head: Optional[ListNode]) -> bool:
  if head == None:
    return False

  tortoise = hare = head

  while tortoise and hare and hare.next:
    tortoise = tortoise.next
    hare = hare.next.next

    if tortoise == hare:
      return True

  return False