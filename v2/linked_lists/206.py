from typing import Optional, List
from LinkedList import ListNode, LinkedList

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    
    prev = head
    curr = prev.next

    # Rearranging happens from the LL @ the 1st idx.
    # NOTE: Not necessary if `curr` is init. set to the `head`.
    head.next = None

    while curr:
        tmp = curr.next

        curr.next = prev
        prev = curr
        curr = tmp

    return prev

LL = LinkedList()
LL.printLL(LL.createLL([0, 1, 2, 3]))
LL.printLL(reverseList(LL.createLL([0, 1, 2, 3])))
LL.printLL(reverseList(LL.createLL([3])))