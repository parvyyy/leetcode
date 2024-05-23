from typing import Optional, ListNode

def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  head = curr = ListNode()

  while l1 and l2:
    if l1.val > l2.val:
      curr.next = ListNode(l1.val)
      l1 = l1.next
    elif l2.val > l1.val:
      curr.next = ListNode(l2.val)
      l2 = l2.next

    curr = curr.next

  while l1:
    curr.next = ListNode(l1.val)
    l1, curr = l1.next, curr.next

  while l2:
    curr.next = ListNode(l2.val)
    l2, curr = l2.next, curr.next

  return head.next