from LinkedList import ListNode
from typing import Optional

# Hashset
def hasCycle(head: Optional[ListNode]) -> bool:
    seen = set()

    curr = head

    while curr:
        if curr in seen:
            return True
        
        seen.add(curr)
        curr = curr.next

    return False

# Floyd's Cycle Detection
# If a cycle exists then the fast pointer
# (one) which traverses as twice the speed
# should eventually "lap" the slow pointer.

# The primary benefit is an O(1) time complexity.
def hasCycle(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
        
    return False