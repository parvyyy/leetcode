from LinkedList import ListNode, LinkedList
from typing import Optional

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    curr1, curr2 = l1, l2

    head = ListNode()
    curr = head

    carry = 0
    while curr1 or curr2 or carry > 0:
        # Only the carry remains
        if not curr1 and not curr2:
            curr.next = ListNode(carry)
            curr = curr.next
            carry = 0

        elif not curr1:
            summ = curr2.val + carry
            v, carry = summ % 10, summ // 10

            curr.next = ListNode(v)
            curr = curr.next

            curr2 = curr2.next

        elif not curr2:
            summ = curr1.val + carry
            v, carry = summ % 10, summ // 10

            curr.next = ListNode(v)
            curr = curr.next

            curr1 = curr1.next
        else:
            summ = curr1.val + curr2.val + carry
            v, carry = summ % 10, summ // 10

            curr.next = ListNode(v)
            curr = curr.next

            curr1 = curr1.next
            curr2 = curr2.next

    return head.next

LL = LinkedList()

LL.printLL(addTwoNumbers(LL.createLL([1, 2, 3]), LL.createLL([4, 5, 6])))
LL.printLL(addTwoNumbers(LL.createLL([9]), LL.createLL([9])))