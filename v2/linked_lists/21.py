from LinkedList import ListNode, LinkedList
from typing import Optional

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    h1, h2 = list1, list2
    
    head = ListNode()
    curr = head

    while h1 and h2:
        if h1.val <= h2.val:
            curr.next = h1
            h1 = h1.next
        else:
            curr.next = h2
            h2 = h2.next
        
        curr = curr.next
    
    # Handles when one reaches None earlier
    curr.next = h1 if h1 else h2

    return head.next

LL = LinkedList()
LL.printLL(mergeTwoLists(LL.createLL([1, 2, 4]), LL.createLL([1, 3, 5])))