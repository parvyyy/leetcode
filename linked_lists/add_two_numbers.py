from typing import Optional, ListNode

def length(l: Optional[ListNode]) -> int:
  length = 0
  
  while l:
    length += 1

  return length


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  n, m = length(l1), length(l2)

  head = curr = ListNode(0, None)

  # Add the leading values of the longer list to tot.
  if n > m:
    for j in range(n):
      curr.next = ListNode(l1.val)
      curr, l1 = curr.next, l1.next
  elif m > n:
    for j in range(m):
      curr.next = ListNode(l2.val)
      curr, l2 = curr.next, l2.next

  # Progress to the start.
  head = head.next

  # Initially, there is no carried term as the value (a digit) in a singular list
  # cannot exceed 10.
  carry = 0

  while l1 and l2:
    rem = (l1.val + l2.val) % 10

    curr.next = ListNode(rem + carry)

    carry = (l1.val + l2.val) // 10

    curr, l1, l2 = curr.next, l1.next, l2.next

  return head