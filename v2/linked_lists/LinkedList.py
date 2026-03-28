from typing import Optional, List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    @staticmethod
    def printLL(head: Optional[ListNode]) -> None:
        curr = head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()

    @staticmethod
    def createLL[T](ls: List[T]) -> Optional[ListNode]:
        n = len(ls)

        if n == 0:
            return None

        head = ListNode(ls[0])
        curr = head
        for v in ls[1:]:
            curr.next = ListNode(v)
            curr = curr.next

        return head