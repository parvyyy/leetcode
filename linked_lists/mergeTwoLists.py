class ListNode(object):
     def __init__(self, val = 0, next = None):
         self.val = val
         self.next = next
    
def mergeTwoLists(list1, list2):
     head1, head2 = list1, list2

     if head1 is None:
          return list2
     
     if head2 is None:
          return list1
     
     # 'Node' will be the travelling ptr. 'Dummy will be a pointing to the
     # head of the merged LL.
     dummy = node = ListNode()
     
     while head1 is not None and head2 is not None:
          if (head1.val <= head2.val):
               # Create next node
               node.next = ListNode(head1.val, None)
               head1 = head1.next
          else:
               # Create next node
               node.next = ListNode(head2.val, None)
               head2 = head2.next
          
          # Increments the merged LL pointer to the latest element.
          node = node.next
     
     # Add the leftover elements into merged. This can be done by simply linking
     # the end of the current merged LL to the traversal ptr of the longer LL.
     if head1:
          node.next = head1

     if head2:
          node.next = head2
          
     return dummy.next

def main():
     merged_list = mergeTwoLists(ListNode(1, ListNode(2, ListNode(4, None))), ListNode(1, ListNode(3, ListNode(4, None))))

     ans = ''
     while merged_list:
          ans += str(merged_list.val) + ' '
          merged_list = merged_list.next

     print(ans)
     return 0

if __name__ == "__main__":
    main()