from LinkedList import ListNode, LinkedList
from typing import Optional

def reorderList(head: Optional[ListNode]) -> None:
    def length(head: Optional[ListNode]) -> int:
        curr, n = head, 0

        while curr:
            curr = curr.next
            n += 1

        return n

    n = length(head)
    n0 = 0
    curr, prev = head, None

    while curr:
        tmp = curr.next

        # Prevent a cycle
        if n0 == n // 2:
            curr.next = None

        # Reverse secondary half of the LL.    
        if n0 > n // 2:
            curr.next = prev

        prev = curr
        curr = tmp

        n0 += 1

    end = prev
    start = head

    # Flip flop between connecting start to end & end to start.
    is_start = 0

    while start != end:
        if is_start % 2 == 0:
            tmp = start.next

            start.next = end
            start = tmp
        else:
            tmp = end.next

            end.next = start
            end = tmp

        is_start += 1

    return head


LL = LinkedList()

head = reorderList(LL.createLL([2, 4, 6, 8, 10]))
LL.printLL(head)

head = reorderList(LL.createLL([2, 4, 6, 8]))
LL.printLL(head)
