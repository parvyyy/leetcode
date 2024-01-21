class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
def mergeTwoLists(list1, list2):
     head1, head2 = list1, list2

     if head1 is None:
          return list2
     
     if head2 is None:
          return list1
     
     node = None
     merged_head = None

     while head1 is not None and head2 is not None:
          if (head1.val <= head2.val):
               if not node:
                    node = ListNode(head1.val, None)
                    merged_head = node
               else:
                    node.next = ListNode(head1.val, None)
                    node = node.next

               head1 = head1.next
          else:
               if not node:
                    node = ListNode(head2.val, None)
                    merged_head = node
               else:
                    node.next = ListNode(head2.val, None)
                    node = node.next

               head2 = head2.next
     
     # Add the leftover elements into merged
     while head1 is not None:
          node.next = ListNode(head1.val, None)
          head1 = head1.next
          node = node.next
     
     while head2 is not None:
          node.next = ListNode(head2.val, None)
          head2 = head2.next
          node = node.next
          
     return merged_head

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