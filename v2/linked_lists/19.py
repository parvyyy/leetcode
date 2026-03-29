from LinkedList import ListNode, LinkedList
from typing import Optional

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def length(head: Optional[ListNode]) -> int:
        curr, n = head, 0

        while curr:
            n += 1
            curr = curr.next

        return n
    
    # N-th index from the start.
    n, n0 = length(head) - n, 0
    curr, prev = head, None

    while curr:
        if n == n0:
            # Handle removing the `head`
            if curr == head:
                return head.next

            prev.next = curr.next
            curr.next = None
            return head

        # Progress pointers
        prev = curr
        curr = curr.next
        n0 += 1

    return head