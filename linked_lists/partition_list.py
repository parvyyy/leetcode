from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
  new_head = curr = ListNode()
  
  follower = head
  while follower:
    if follower.val < x:
      curr.next = ListNode(follower.val)
      curr = curr.next
      
    follower = follower.next

  follower = head
  while follower:
    if follower.val >= x:
      curr.next = ListNode(follower.val)
      curr = curr.next
      
    follower = follower.next

  return new_head.next