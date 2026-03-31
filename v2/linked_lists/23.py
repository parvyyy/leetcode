from typing import Optional, List
from LinkedList import ListNode, LinkedList

# NOTE: This solution has an O(n * k) time complexity.
#       However, we can opt for a divide-and-conquer
#       approach to acheive O(n * log(k))
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    n = len(lists)

    if n == 0:
        return None
    
    if n == 1:
        return lists[0]
    
    l1 = lists[0]

    def mergeLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        curr = head

        while l1 or l2:
            if not l1:
                curr.next = l2
                break

            if not l2:
                curr.next = l1
                break

            if l1.val <= l2.val:
                curr.next = l1
                l1, curr = l1.next, curr.next
            else:
                curr.next = l2
                l2, curr = l2.next, curr.next

        return head.next

    for i in range(1, n):
        l1 = mergeLists(l1, lists[i])

    return l1

def mergeKListsV2(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    n = len(lists)

    if n == 0:
        return None
    
    if n == 1:
        return lists[0]
    
    def mergeLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        curr = head

        while l1 or l2:
            if not l1:
                curr.next = l2
                break

            if not l2:
                curr.next = l1
                break

            if l1.val <= l2.val:
                curr.next = l1
                l1, curr = l1.next, curr.next
            else:
                curr.next = l2
                l2, curr = l2.next, curr.next

        return head.next

    # Merges pairs, totalling `log(k)` steps.
    while True:
        n = len(lists)
        if n == 1:
            break

        merged = []
        for i in range(0, n, 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < n else None

            merged.append(mergeLists(l1, l2))

        lists = merged

    return lists[0]

LL = LinkedList()
LL.printLL(mergeKLists([LL.createLL([1, 2, 4]), LL.createLL([1, 3, 5]), LL.createLL([3, 6])]))


