from typing import Optional
from LinkedList import ListNode, LinkedList

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def length(curr: Optional[ListNode]) -> int:
        n = 0

        while curr:
            n += 1
            curr = curr.next

        return n

    def getKth(curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        k0 = 1

        while curr and k0 < k:
            k0 += 1
            curr = curr.next

        if k0 < k:
            return None
        
        return curr

    n = length(head)
    n_groups = n // k

    curr = head

    # The new head will be the k-th element.
    head = getKth(curr, k)

    for _ in range(n_groups):
        # `curr` points to the i * k-th element.
        # `head_prime` represents the local `head` 
        # of the current `k` elements in the LL.
        head_prime, prev, k0 = curr, None, 0

        # Swaps `k` elements.
        while k0 < k:
            tmp = curr.next

            curr.next = prev
            
            prev = curr
            curr = tmp
            k0 += 1

        # Map the original start to the k-th element in
        # the next set
        if kth := getKth(curr, k):
            head_prime.next = kth
            continue
        
        # Otherwise, there are less than `k` values
        # hence, attach the remainder of the LL.
        head_prime.next = curr

    return head

LL = LinkedList()

LL.printLL(reverseKGroup(LL.createLL([1, 2, 3, 4, 5, 6]), 3))
LL.printLL(reverseKGroup(LL.createLL([1, 2, 3, 4, 5]), 3))